import logging
import schedule
import time
import datetime
import boto3
import json
import os
import redisdb
import user_utils
import secrets
import sentry_sdk
import cloudlanguagetools.servicemanager

def backup_redis_db():
    try:
        logging.info('backing up redis db')
        connection = redisdb.RedisDb()

        session = boto3.session.Session()
        client = session.client('s3',
                                region_name=os.environ['SPACE_REGION'],
                                endpoint_url=os.environ['SPACE_ENDPOINT_URL'],
                                aws_access_key_id=os.environ['SPACE_KEY'],
                                aws_secret_access_key=os.environ['SPACE_SECRET'])    
        bucket_name = 'cloud-language-tools-redis-backups'

        full_db_dump = connection.full_db_dump()
        time_str = datetime.datetime.now().strftime('%H')
        file_name = f'redis_backup_{time_str}.json'
        client.put_object(Body=str(json.dumps(full_db_dump)), Bucket=bucket_name, Key=file_name)
        logging.info(f'wrote {file_name} to {bucket_name}')
    except:
        logging.exception(f'could not backup redis db')


def update_airtable():
    try:
        logging.info('updating airtable')
        utils = user_utils.UserUtils()
        utils.update_airtable_all()
        logging.info('finished updating airtable')
    except:
        logging.exception(f'could not update airtable')    

def report_getcheddar_usage():
    try:
        logging.info('reporting getcheddar usage')
        utils = user_utils.UserUtils()
        utils.report_getcheddar_usage_all_users()
        logging.info('finished reporting getcheddar usage')
    except:
        logging.exception(f'could not report getcheddar usage')

def update_language_data():
    try:    
        logging.info('udpating language data')
        manager = cloudlanguagetools.servicemanager.ServiceManager(secrets.config)
        manager.configure()
        language_data = manager.get_language_data_json()
        redis_connection = redisdb.RedisDb()
        redis_connection.store_language_data(language_data)
    except:
        logging.exception(f'could not update language_data')

def setup_tasks():
    logging.info('running tasks once')
    if secrets.config['scheduled_tasks']['user_data']:
        logging.info('setting up user_data tasks')
        report_getcheddar_usage()
        update_airtable()
        schedule.every(15).minutes.do(update_airtable)
        schedule.every(6).hours.do(report_getcheddar_usage)
    if secrets.config['scheduled_tasks']['backup_redis']:
        logging.info('setting up redis_backup')
        backup_redis_db()
        schedule.every(1).hour.do(backup_redis_db)
    if secrets.config['scheduled_tasks']['language_data']:
        logging.info('setting up language_data')
        update_language_data()
        schedule.every(3).hours.do(update_language_data)


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                        datefmt='%Y%m%d-%H:%M:%S',
                        level=logging.INFO,
                        handlers=[logging.StreamHandler()])

    if secrets.config['sentry']['enable']:
        dsn = secrets.config['sentry']['dsn']
        sentry_sdk.init(
            dsn=dsn,
            environment=secrets.config['sentry']['environment'],
            traces_sample_rate=1.0
        )

    setup_tasks()
    run_scheduler()