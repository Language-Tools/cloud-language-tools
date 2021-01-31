#!/usr/bin/env python3

from flask import Flask, request, send_file, jsonify, make_response
import flask_restful
import json
import functools
import os
import logging
import cloudlanguagetools.servicemanager
import cloudlanguagetools.errors
import redisdb
import patreon_utils

#logging.basicConfig()
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                    datefmt='%Y%m%d-%H:%M:%S',
                    level=logging.INFO)

app = Flask(__name__)
api = flask_restful.Api(app)

manager = cloudlanguagetools.servicemanager.ServiceManager()
manager.configure()

redis_connection = redisdb.RedisDb()

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

def track_usage(request_type, request):
    api_key = request.headers.get('api_key', None)
    if api_key != None:
        text = request.json['text']
        characters = len(text)
        service = request.json['service']
        redis_connection.track_usage(api_key, service, request_type, characters)

def track_usage_translation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        track_usage('translation', request)
        return func(*args, **kwargs)
    return wrapper        

def track_usage_transliteration(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        track_usage('transliteration', request)
        return func(*args, **kwargs)
    return wrapper            

def track_usage_audio(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        track_usage('audio', request)
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
    method_decorators = [authenticate, track_usage_translation]
    def post(self):
        try:
            data = request.json
            return {'translated_text': manager.get_translation(data['text'], data['service'], data['from_language_key'], data['to_language_key'])}
        except cloudlanguagetools.errors.RequestError as err:
            return {'error': str(err)}, 400

class TranslateAll(flask_restful.Resource):
    method_decorators = [authenticate]
    def post(self):
        try:
            data = request.json
            return manager.get_all_translations(data['text'], data['from_language'], data['to_language'])
        except cloudlanguagetools.errors.RequestError as err:
            return {'error': str(err)}, 400

class Transliterate(flask_restful.Resource):
    method_decorators = [authenticate, track_usage_transliteration]
    def post(self):
        try:
            data = request.json
            return {'transliterated_text': manager.get_transliteration(data['text'], data['service'], data['transliteration_key'])}
        except cloudlanguagetools.errors.RequestError as err:
            return {'error': str(err)}, 400    

class Detect(flask_restful.Resource):
    method_decorators = [authenticate]
    def post(self):
        data = request.json
        text_list = data['text_list']
        result = manager.detect_language(text_list)
        return {'detected_language': result.name}

class Audio(flask_restful.Resource):
    method_decorators = [authenticate, track_usage_audio]
    def post(self):
        data = request.json
        audio_temp_file = manager.get_tts_audio(data['text'], data['service'], data['voice_key'], data['options'])
        return send_file(audio_temp_file.name, mimetype='audio/mpeg')

class VerifyApiKey(flask_restful.Resource):
    def post(self):
        data = request.json
        api_key = data['api_key']
        result = redis_connection.api_key_valid(api_key)
        return result

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
        patreon_client_id = os.environ['PATREON_CLIENT_ID']
        redirect_uri = os.environ['PATREON_REDIRECT_URI']
        oauth_request_link = f'https://www.patreon.com/oauth2/authorize?response_type=code&client_id={patreon_client_id}&redirect_uri={redirect_uri}&scope=identity%20identity%5Bemail%5D'
        result_html = f'Click here to request your AwesomeTTS Plus / Language Tools API Key: <a href="{oauth_request_link}">Connect with Patreon</a>'
        return make_response(result_html, 200, headers)

api.add_resource(LanguageList, '/language_list')
api.add_resource(VoiceList, '/voice_list')
api.add_resource(TranslationLanguageList, '/translation_language_list')
api.add_resource(TransliterationLanguageList, '/transliteration_language_list')
api.add_resource(Translate, '/translate')
api.add_resource(TranslateAll, '/translate_all')
api.add_resource(Transliterate, '/transliterate')
api.add_resource(Detect, '/detect')
api.add_resource(Audio, '/audio')
api.add_resource(VerifyApiKey, '/verify_api_key')
api.add_resource(PatreonKey, '/patreon_key')
api.add_resource(PatreonKeyRequest, '/request_patreon_key')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')