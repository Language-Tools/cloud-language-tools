import os
import time
import datetime
import redis

ENV_VAR_REDIS_URL = 'REDIS_URL'

KEY_TYPE_API_KEY = 'api_key'

class RedisDb():
    def __init__(self):
        self.connect()

    def connect(self, db_num=0):
        redis_url = os.environ[ENV_VAR_REDIS_URL]

        self.r = redis.from_url(redis_url, db=db_num)

    def build_key(self, key_type, key):
        return f'clt:{key_type}:{key}'

    def add_api_key(self, api_key, key_type, owner, expiration_date):
        key_removal_date = expiration_date + datetime.timedelta(days=31)
        key_expiration_timestamp = int(expiration_date.timestamp())
        key_removal_timestamp_millis = int(key_removal_date.timestamp() * 1000.0)
        redis_key = self.build_key(KEY_TYPE_API_KEY, api_key)
        hash_value = {
            'key_type': key_type,
            'owner': owner,
            'expiration': key_expiration_timestamp,
        }
        self.r.hset(redis_key, mapping=hash_value)
        self.r.expireat(redis_key, key_removal_timestamp_millis)

        print(f'added {redis_key}: {hash_value}, expiring at: {expiration_date}, removed at: {key_removal_date}')

    def api_key_valid(self, api_key):
        redis_key = self.build_key(KEY_TYPE_API_KEY, api_key)
        if self.r.exists(redis_key) == 0:
            return {'key_valid': False, 'msg': 'API Key not valid'}
        key_data = self.r.hgetall(redis_key)
        expiration = self.r.hget(redis_key, 'expiration')
        expiration_timestamp = int(self.r.hget(redis_key, 'expiration'))
        current_dt = datetime.datetime.now()
        current_timestamp = int(current_dt.timestamp())
        expiration_dt = datetime.datetime.fromtimestamp(expiration_timestamp)
        if expiration_timestamp > current_timestamp:
            expire_time_delta = expiration_dt - current_dt
            return {'key_valid': True, 'msg': f'API Key expires in {expire_time_delta.days} days'}
        return {'key_valid': False, 'msg':f'API Key expired'}
        
    def list_api_keys(self):
        pattern = self.build_key(KEY_TYPE_API_KEY, '*')
        cursor, keys = self.r.scan(match=pattern)
        for key in keys:
            key_str = key.decode('utf-8')
            api_key = key_str.split(':')[-1]
            validity = self.api_key_valid(api_key)
            # print(key)
            key_data = self.r.hgetall(key)
            print(f'{api_key} {key_data}, {validity}')

    def list_all_keys(self):
        cursor, keys = self.r.scan()
        for key in keys:
            print(key)

    def clear_db(self, wait=True):
        if wait:
            print('WARNING! going to remove all keys after 30s')
            time.sleep(15)
            print('WARNING! going to remove all keys after 15s')
            time.sleep(15)
        self.r.flushdb()