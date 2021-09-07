#!/usr/bin/env python3

from flask import Flask, request, send_file, jsonify, make_response
import flask_restful
import json
import functools
import os
import sys
import logging
import urllib.parse
import cloudlanguagetools.constants
import cloudlanguagetools.servicemanager
import cloudlanguagetools.errors
import redisdb
import patreon_utils
import getcheddar_utils as getcheddar_utils_module
import convertkit
import secrets
import quotas
import pprint
import hashlib
import hmac
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

#logging.basicConfig()
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                    datefmt='%Y%m%d-%H:%M:%S',
                    level=logging.INFO)

if secrets.config['sentry']['enable']:
    dsn = secrets.config['sentry']['dsn']
    sentry_sdk.init(
        dsn=dsn,
        environment=secrets.config['sentry']['environment'],
        integrations=[FlaskIntegration()],
        traces_sample_rate=0.2
    )



app = Flask(__name__)
api = flask_restful.Api(app)

manager = cloudlanguagetools.servicemanager.ServiceManager(secrets.config)
manager.configure()

redis_connection = redisdb.RedisDb()
convertkit_client = convertkit.ConvertKit()
getcheddar_utils = getcheddar_utils_module.GetCheddarUtils()

def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('api_key', None)
        # is this API key valid ?
        result = redis_connection.api_key_valid(api_key)
        if result['key_valid']:
            # authentication successful
            return func(*args, **kwargs)
        return {'error': result['msg']}, 401
    return wrapper

def authenticate_get(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.args.get('api_key', None)
        # is this API key valid ?
        result = redis_connection.api_key_valid(api_key)
        if result['key_valid']:
            # authentication successful
            return func(*args, **kwargs)
        return {'error': result['msg']}, 401
    return wrapper

def track_usage(request_type, request, func, *args, **kwargs):
    api_key = request.headers.get('api_key', None)
    if api_key != None:
        text = request.json.get('text', None)
        service_str = request.json.get('service', None)
        if text != None and service_str != None:
            service = cloudlanguagetools.constants.Service[service_str]
            characters = len(text)

            # try to get language_code
            language_code = None
            language_code_str = request.json.get('language_code', None)
            if language_code_str != None:
                language_code = cloudlanguagetools.constants.Language[language_code_str]

            try:
                redis_connection.track_usage(api_key, service, request_type, characters, language_code)
            except cloudlanguagetools.errors.OverQuotaError as err:
                return {'error': str(err)}, 429
    return func(*args, **kwargs)

def track_usage_translation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return track_usage(cloudlanguagetools.constants.RequestType.translation, request, func, *args, **kwargs)
    return wrapper        

def track_usage_transliteration(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return track_usage(cloudlanguagetools.constants.RequestType.transliteration, request, func, *args, **kwargs)
    return wrapper            

def track_usage_audio(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return track_usage(cloudlanguagetools.constants.RequestType.audio, request, func, *args, **kwargs)
    return wrapper            

def track_usage_audio_yomichan(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.args.get('api_key', None)
        if api_key != None:
            text = request.args.get('text', None)
            service_str = request.args.get('service', None)
            if text != None and service_str != None:
                service = cloudlanguagetools.constants.Service[service_str]
                characters = len(text)
                try:
                    redis_connection.track_usage(api_key, service, cloudlanguagetools.constants.RequestType.audio, characters, cloudlanguagetools.constants.Language.ja)
                except cloudlanguagetools.errors.OverQuotaError as err:
                    return {'error': str(err)}, 429
        return func(*args, **kwargs)
    return wrapper


class LanguageList(flask_restful.Resource):
    def get(self):
        return manager.get_language_list()

class VoiceList(flask_restful.Resource):
    def get(self):
        return manager.get_tts_voice_list_json()

class TranslationLanguageList(flask_restful.Resource):
    def get(self):
        return manager.get_translation_language_list_json()

class TransliterationLanguageList(flask_restful.Resource):
    def get(self):
        return manager.get_transliteration_language_list_json()

class Translate(flask_restful.Resource):
    method_decorators = [track_usage_translation, authenticate]
    def post(self):
        try:
            data = request.json
            # add sentry service tag
            sentry_sdk.set_tag("clt.service", data['service'])
            return {'translated_text': manager.get_translation(data['text'], data['service'], data['from_language_key'], data['to_language_key'])}
        except cloudlanguagetools.errors.RequestError as err:
            sentry_sdk.capture_exception(err)
            return {'error': str(err)}, 400

class TranslateAll(flask_restful.Resource):
    method_decorators = [authenticate]
    def post(self):
        try:
            data = request.json
            return manager.get_all_translations(data['text'], data['from_language'], data['to_language'])
        except cloudlanguagetools.errors.RequestError as err:
            sentry_sdk.capture_exception(err)
            return {'error': str(err)}, 400

class Transliterate(flask_restful.Resource):
    method_decorators = [track_usage_transliteration, authenticate]
    def post(self):
        try:
            data = request.json
            # add sentry service tag
            sentry_sdk.set_tag("clt.service", data['service'])
            return {'transliterated_text': manager.get_transliteration(data['text'], data['service'], data['transliteration_key'])}
        except cloudlanguagetools.errors.RequestError as err:
            sentry_sdk.capture_exception(err)
            return {'error': str(err)}, 400    

class Detect(flask_restful.Resource):
    method_decorators = [authenticate]
    def post(self):
        data = request.json
        text_list = data['text_list']
        result = manager.detect_language(text_list)
        return {'detected_language': result.name}

class Audio(flask_restful.Resource):
    method_decorators = [track_usage_audio, authenticate] # authenticate is the first step
    def post(self):
        try:
            data = request.json
            audio_temp_file = manager.get_tts_audio(data['text'], data['service'], data['voice_key'], data['options'])
            return send_file(audio_temp_file.name, mimetype='audio/mpeg')
        except cloudlanguagetools.errors.NotFoundError as err:
            return {'error': str(err)}, 404
        except cloudlanguagetools.errors.RequestError as err:
            sentry_sdk.capture_exception(err)
            return {'error': str(err)}, 400


class AudioV2(flask_restful.Resource):
    method_decorators = [track_usage_audio, authenticate] # authenticate is the first step
    def post(self):
        try:

            # generate audio data
            data = request.json
            text = data['text']
            service_str = data['service']
            request_mode_str = data['request_mode']
            language = data['language_code']
            voice_key = data['voice_key']
            options = data['options']

            if len(text) == 0:
                return {'error': 'empty text'}, 400

            # convert to enum
            language_code = cloudlanguagetools.constants.Language[language]
            service = cloudlanguagetools.constants.Service[service_str]
            request_mode = cloudlanguagetools.constants.RequestMode[request_mode_str]

            # add sentry service tag
            sentry_sdk.set_tag("clt.service", service.name)

            audio_temp_file = manager.get_tts_audio(text, service.name, voice_key, options)

            # track client
            api_key = request.headers.get('api_key')
            client = request.headers.get('client')
            version = request.headers.get('client_version')
            redis_connection.track_client(api_key, client, version)

            # track request mode
            redis_connection.track_request_mode(api_key, request_mode)

            # track service
            redis_connection.track_service(api_key, service)

            # track audio language
            redis_connection.track_audio_language(api_key, language_code)

            # return data
            return send_file(audio_temp_file.name, mimetype='audio/mpeg')
        except cloudlanguagetools.errors.NotFoundError as err:
            return {'error': str(err)}, 404
        except cloudlanguagetools.errors.RequestError as err:
            sentry_sdk.capture_exception(err)
            return {'error': str(err)}, 400            

class YomichanAudio(flask_restful.Resource):
    method_decorators = [track_usage_audio_yomichan, authenticate_get]
    def get(self):
        try:
            source_text = request.args.get('text')
            service = request.args.get('service')
            voice_key_urlencode_str = request.args.get('voice_key')
            if source_text == None or service == None or voice_key_urlencode_str == None:
                return {'error': 'missing arguments'}, 400
            voice_key_json_str = urllib.parse.unquote_plus(voice_key_urlencode_str)
            voice_key = json.loads(voice_key_json_str)
            options = {}
            audio_temp_file = manager.get_tts_audio(source_text, service, voice_key, options)
            return send_file(audio_temp_file.name, mimetype='audio/mpeg')
        except cloudlanguagetools.errors.RequestError as err:
            sentry_sdk.capture_exception(err)
            return {'error': str(err)}, 400        


class VerifyApiKey(flask_restful.Resource):
    def post(self):
        data = request.json
        api_key = data['api_key']
        result = redis_connection.api_key_valid(api_key)
        return result

class Account(flask_restful.Resource):
    def get(self):
        api_key = request.headers.get('api_key')
        account_data = redis_connection.get_account_data(api_key)
        return account_data

class PatreonKey(flask_restful.Resource):
    def get(self):
        # www.patreon.com/oauth2/authorize?response_type=code&client_id=trDOSYhOAtp3MRuBhaZgnfCv4Visg237B2gslK4dha9K780iEClYNBM0QW1OH8MM&redirect_uri=https://4b1c5e33b08b.ngrok.io/patreon_key&scope=identity%20identity%5Bemail%5D

        oauth_code = request.args.get('code')
        result = patreon_utils.user_authorized(oauth_code)

        headers = {'Content-Type': 'text/html'}

        if result['authorized'] == True:
            # locate user key
            api_key = redis_connection.get_patreon_user_key(result['user_id'], result['email'])
            result_html = f"Hello {result['email']}! Thanks for being a fan! Here is your API Key, to use with AwesomeTTS Plus or Language Tools: <b>{api_key}</b>"
            return make_response(result_html, 200, headers)

        return 'You need to be a patreon subscriber to obtain an API key'

class PatreonKeyRequest(flask_restful.Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        patreon_client_id = secrets.config['patreon']['client_id']
        redirect_uri = secrets.config['patreon']['redirect_uri']
        oauth_request_link = f'https://www.patreon.com/oauth2/authorize?response_type=code&client_id={patreon_client_id}&redirect_uri={redirect_uri}&scope=identity%20identity%5Bemail%5D'
        result_html = f'Click here to request your AwesomeTTS Plus / Language Tools API Key: <a href="{oauth_request_link}">Connect with Patreon</a>'
        return make_response(result_html, 200, headers)

class ConvertKitRequestTrialKey(flask_restful.Resource):
    def post(self):
        data = request.json
        subscriber_id = data['subscriber']['id']
        email_address = data['subscriber']['email_address']

        email_valid = convertkit_client.email_valid(email_address)
        if not email_valid:
            convertkit_client.tag_user_disposable_email(email_address)
            return

        # create api key for this subscriber
        api_key = redis_connection.get_trial_user_key(email_address)

        convertkit_client.tag_user_api_ready(email_address, api_key, quotas.TRIAL_USER_CHARACTER_LIMIT)

        logging.info(f'trial key created for {email_address}')

class ConvertKitRequestPatreonKey(flask_restful.Resource):
    def post(self):
        data = request.json
        email_address = data['subscriber']['email_address']
        patreon_id = data['subscriber']['fields']['patreon_user_id']
        logging.info(f'ConvertKitRequestPatreonKey, email: {email_address}, patreon_id: {patreon_id}')

        # create api key for this subscriber
        api_key = redis_connection.get_patreon_user_key(patreon_id, email_address)

        convertkit_client.tag_user_patreon_api_ready(email_address, api_key)

        logging.info(f'patreon key created for {email_address}: {api_key}')

class GetCheddar(flask_restful.Resource):
    def post(self):
        # get content body for verification purposes
        raw_data = request.get_data()
        token = hashlib.md5(raw_data).hexdigest()
        expected_signature = hmac.new(bytes(getcheddar_utils.get_api_secret() , 'utf-8'), msg = bytes(token , 'utf-8'), digestmod = hashlib.sha256).hexdigest()
        actual_signature = request.headers.get('X-CG-SIGNATURE')
        # X-CG-SIGNATURE
        if expected_signature != actual_signature:
            error_message = f'error validating getcheddar request: {request.json}, headers: {request.headers}'
            logging.error(error_message)
            return {'error': str(error_message)}, 400

        data = request.json
        webhook_data = getcheddar_utils.decode_webhook(data)
        if webhook_data['type'] == 'customerDeleted':
            # delete user from redis
            redis_connection.delete_getcheddar_user(webhook_data['code'])
            return
        user_data = webhook_data.copy()
        del user_data['type']
        if webhook_data['type'] == 'subscriptionCanceled':
            # don't retain the "thousand_char_used" member as it's 0
            # it will get set correctly when reporting usage
            del user_data['thousand_char_used']
        api_key = redis_connection.get_update_getcheddar_user_key(user_data)
        if webhook_data['type'] == 'newSubscription':
            email = webhook_data['email']
            convertkit_client.register_getcheddar_user(email, api_key)




api.add_resource(LanguageList, '/language_list')
api.add_resource(VoiceList, '/voice_list')
api.add_resource(TranslationLanguageList, '/translation_language_list')
api.add_resource(TransliterationLanguageList, '/transliteration_language_list')
api.add_resource(Translate, '/translate')
api.add_resource(TranslateAll, '/translate_all')
api.add_resource(Transliterate, '/transliterate')
api.add_resource(Detect, '/detect')
api.add_resource(Audio, '/audio')
api.add_resource(AudioV2, '/audio_v2')
api.add_resource(YomichanAudio, '/yomichan_audio')
api.add_resource(VerifyApiKey, '/verify_api_key')
api.add_resource(Account, '/account')
api.add_resource(PatreonKey, '/patreon_key')
api.add_resource(PatreonKeyRequest, '/request_patreon_key')

# convertkit webhooks
api.add_resource(ConvertKitRequestTrialKey, '/convertkit_subscriber_request_trial_key')
api.add_resource(ConvertKitRequestPatreonKey, '/convertkit_subscriber_request_patreon_key')

# getcheddar webooks
api.add_resource(GetCheddar, '/getcheddar')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')