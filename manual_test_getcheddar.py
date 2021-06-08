import unittest
import json
import tempfile
import magic
import datetime
import logging
import pytest
import os
import requests
import urllib.parse
import datetime
import time
import sys

import redisdb
import getcheddar_utils
import user_utils
import cloudlanguagetools.constants

# this test requires webhooks from getcheddar to go through

SLEEP_TIME = 0.1
MAX_WAIT_CYCLES = 25

class GetCheddarEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(GetCheddarEndToEnd, cls).setUpClass()

        logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                            datefmt='%Y%m%d-%H:%M:%S',
                            #stream=sys.stdout,
                            level=logging.DEBUG)        

        # url for cloud language tools
        cls.base_url = 'http://localhost:5000'
        cls.client_version = 'test'

        # setup redis connection
        cls.redis_connection = redisdb.RedisDb()
        cls.redis_connection.clear_db(wait=False)

        # helper classes
        cls.getcheddar_utils = getcheddar_utils.GetCheddarUtils()

        cls.customer_code_timestamp_offset = 0


    @classmethod
    def tearDownClass(cls):
        pass

    def get_customer_code(self):
        timestamp = int(datetime.datetime.now().timestamp()) + self.customer_code_timestamp_offset
        customer_code = f'languagetools+development.language_tools.customer-{timestamp}@mailc.net'
        self.customer_code_timestamp_offset +=1
        return customer_code


    def test_endtoend_signup_quotas(self):
        # create a user
        # pytest manual_test_getcheddar.py -rPP -k test_endtoend_signup_quotas

        customer_code = self.get_customer_code()

        # create the user
        # ===============

        self.getcheddar_utils.create_test_customer(customer_code, customer_code, 'Test', 'Customer', 'SMALL')

        redis_getcheddar_user_key = self.redis_connection.build_key(redisdb.KEY_TYPE_GETCHEDDAR_USER, customer_code)
        max_wait_cycles = MAX_WAIT_CYCLES
        while not self.redis_connection.r.exists(redis_getcheddar_user_key) and max_wait_cycles > 0:
            time.sleep(SLEEP_TIME)
            max_wait_cycles -= 1

        # ensure redis keys got created correctly
        # ---------------------------------------

        self.assertTrue(self.redis_connection.r.exists(redis_getcheddar_user_key))
        api_key = self.redis_connection.r.get(redis_getcheddar_user_key)
        print(f'api_key: {api_key}')
        
        actual_user_data = self.redis_connection.get_getcheddar_user_data(customer_code)
        expected_user_data = {
            'type': 'getcheddar',
            'code': customer_code,
            'email': customer_code,
            'thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 0
        }
        self.assertEqual(actual_user_data, expected_user_data)

        # log some usage (fake)
        # =====================
        service = cloudlanguagetools.constants.Service.Azure
        language_code = cloudlanguagetools.constants.Language.fr
        request_type = cloudlanguagetools.constants.RequestType.audio
        characters = 100000
        # should not throw
        print(f'logging {characters} characters of usage')
        self.redis_connection.track_usage(api_key, service, request_type, characters, language_code=language_code)

        characters = 140000
        # should not throw either
        print(f'logging {characters} characters of usage')
        self.redis_connection.track_usage(api_key, service, request_type, characters, language_code=language_code)

        characters = 10001
        # this one should throw
        print(f'logging {characters} characters of usage')
        self.assertRaises(
            cloudlanguagetools.errors.OverQuotaError, 
            self.redis_connection.track_usage, api_key, service, request_type, characters, language_code=language_code)

        # upgrade to medium plan
        # ======================
        self.getcheddar_utils.update_test_customer(customer_code, 'MEDIUM')
        upgrade_done = False
        max_wait_cycles = MAX_WAIT_CYCLES
        while upgrade_done == False and max_wait_cycles > 0:
            # retrieve customer data
            actual_user_data = self.redis_connection.get_getcheddar_user_data(customer_code)
            upgrade_done = actual_user_data['thousand_char_quota'] == 500
            time.sleep(SLEEP_TIME)
            max_wait_cycles -= 1
        self.assertEqual(upgrade_done, True)

        # log some more usage after upgrade
        # ---------------------------------
        characters = 255000
        # should not throw either
        self.redis_connection.track_usage(api_key, service, request_type, characters, language_code=language_code)        

        # log some more usage, which will throw
        characters = 6000
        # this one should throw
        self.assertRaises(
            cloudlanguagetools.errors.OverQuotaError, 
            self.redis_connection.track_usage, api_key, service, request_type, characters, language_code=language_code)        

        # upgrade to large plan
        # =====================
        self.getcheddar_utils.update_test_customer(customer_code, 'LARGE')
        upgrade_done = False
        max_wait_cycles = MAX_WAIT_CYCLES
        while upgrade_done == False and max_wait_cycles > 0:
            # retrieve customer data
            actual_user_data = self.redis_connection.get_getcheddar_user_data(customer_code)
            upgrade_done = actual_user_data['thousand_char_quota'] == 1000
            time.sleep(SLEEP_TIME)
            max_wait_cycles -= 1
        self.assertEqual(upgrade_done, True)        

        # should not throw
        characters = 500000
        self.redis_connection.track_usage(api_key, service, request_type, characters, language_code=language_code)                
        characters = 500000
        self.redis_connection.track_usage(api_key, service, request_type, characters, language_code=language_code)                        


        # finally, delete the user
        self.getcheddar_utils.delete_test_customer(customer_code)


    def test_endtoend_report_usage(self):
        # create a user
        # pytest manual_test_getcheddar.py -rPP -k test_endtoend_report_usage

        customer_code = self.get_customer_code()

        # create the user
        # ===============

        self.getcheddar_utils.create_test_customer(customer_code, customer_code, 'Test', 'Customer', 'SMALL')

        redis_getcheddar_user_key = self.redis_connection.build_key(redisdb.KEY_TYPE_GETCHEDDAR_USER, customer_code)
        max_wait_cycles = MAX_WAIT_CYCLES
        while not self.redis_connection.r.exists(redis_getcheddar_user_key) and max_wait_cycles > 0:
            time.sleep(SLEEP_TIME)
            max_wait_cycles -= 1

        # ensure redis keys got created correctly
        # ---------------------------------------

        self.assertTrue(self.redis_connection.r.exists(redis_getcheddar_user_key))
        api_key = self.redis_connection.r.get(redis_getcheddar_user_key)
        print(f'api_key: {api_key}')
        
        actual_user_data = self.redis_connection.get_getcheddar_user_data(customer_code)
        expected_user_data = {
            'type': 'getcheddar',
            'code': customer_code,
            'email': customer_code,
            'thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 0
        }
        self.assertEqual(actual_user_data, expected_user_data)

        # log some usage (fake)
        # =====================
        service = cloudlanguagetools.constants.Service.Azure
        language_code = cloudlanguagetools.constants.Language.fr
        request_type = cloudlanguagetools.constants.RequestType.audio
        characters = 142456
        self.redis_connection.track_usage(api_key, service, request_type, characters, language_code=language_code)

        # check the usage slice, it should contain this usage
        usage_slice = self.redis_connection.get_getcheddar_usage_slice(api_key)
        usage = self.redis_connection.get_usage_slice_data(usage_slice)
        self.assertEqual(usage['characters'], 142456)

        # now, report this usage to getcheddar
        user_utils_instance = user_utils.UserUtils()
        user_utils_instance.report_getcheddar_user_usage(api_key)

        # retrieve user data again
        actual_user_data = self.redis_connection.get_getcheddar_user_data(customer_code)
        expected_user_data = {
            'type': 'getcheddar',
            'code': customer_code,
            'email': customer_code,
            'thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 142.456
        }
        self.assertEqual(actual_user_data, expected_user_data)

        # retrieve the usage slice again, it should have been reset
        usage = self.redis_connection.get_usage_slice_data(usage_slice)
        self.assertEqual(usage['characters'], 0)

        # characters = 140000
        # # should not throw either
        # print(f'logging {characters} characters of usage')
        # self.redis_connection.track_usage(api_key, service, request_type, characters, language_code=language_code)

        # finally, delete the user
        self.getcheddar_utils.delete_test_customer(customer_code)

    def test_new_user_audio(self):
        # create a user
        # pytest manual_test_getcheddar.py -rPP -k test_new_user_audio

        customer_code = self.get_customer_code()

        # create the user
        # ===============

        self.getcheddar_utils.create_test_customer(customer_code, customer_code, 'Test', 'Customer', 'SMALL')

        redis_getcheddar_user_key = self.redis_connection.build_key(redisdb.KEY_TYPE_GETCHEDDAR_USER, customer_code)
        max_wait_cycles = MAX_WAIT_CYCLES
        while not self.redis_connection.r.exists(redis_getcheddar_user_key) and max_wait_cycles > 0:
            time.sleep(SLEEP_TIME)
            max_wait_cycles -= 1

        self.assertTrue(self.redis_connection.r.exists(redis_getcheddar_user_key))
        api_key = self.redis_connection.r.get(redis_getcheddar_user_key)

        # ensure we can retrieve some audio
        # ---------------------------------

        # get voice list
        response = requests.get(f'{self.base_url}/voice_list')
        voice_list = response.json()

        source_text_french = 'Je ne suis pas intéressé.'
        source_text_japanese = 'おはようございます'

        # get one azure voice for french

        service = 'Azure'
        french_voices = [x for x in voice_list if x['language_code'] == 'fr' and x['service'] == service]
        first_voice = french_voices[0]
        response = requests.post(f'{self.base_url}/audio_v2', json={
            'text': source_text_french,
            'service': service,
            'deck_name': 'french_deck_1',
            'request_mode': 'batch',
            'language_code': first_voice['language_code'],
            'voice_key': first_voice['voice_key'],
            'options': {}
        }, headers={'api_key': api_key, 'client': 'test', 'client_version': self.client_version})

        self.assertEqual(response.status_code, 200)

        # retrieve file
        output_temp_file = tempfile.NamedTemporaryFile()
        with open(output_temp_file.name, 'wb') as f:
            f.write(response.content)
        f.close()

        # perform checks on file
        # ----------------------

        # verify file type
        filetype = magic.from_file(output_temp_file.name)
        # should be an MP3 file
        expected_filetype = 'MPEG ADTS, layer III'        

        # finally, delete the user
        self.getcheddar_utils.delete_test_customer(customer_code)



if __name__ == '__main__':
    # how to run with logging on: pytest test_api.py -s -p no:logging -k test_translate
    unittest.main()  