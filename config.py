"""config.py - Application Deployment Settings.
"""

import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class BaseSettings(object):
    DB_HOST = ''
    DB_KEY = ''
    DB_DATABASE = ''
    DEBUG = False
    SESSION_SECRET = os.environ.get('MPJ_SESSION_SECRET')


class ProductionSettings(BaseSettings):
    DB_HOST = os.environ.get('MPJ_PROD_DB_HOST')
    DB_KEY = os.environ.get('MPJ_PROD_DB_KEY')
    DB_DATABASE = os.environ.get('MPJ_PROD_DB_DATABASE')
    DEBUG = False


class DevelopmentSettings(BaseSettings):
    DB_HOST = os.environ.get('MPJ_DEV_DB_HOST')
    DB_KEY = os.environ.get('MPJ_DEV_DB_KEY')
    DB_DATABASE = os.environ.get('MPJ_DEV_DB_DATABASE')
    DEBUG = True


deploy = os.environ.get('MPJ_ENVIRONMENT', 'DEVELOPMENT')
if deploy == 'PRODUCTION':
    config = ProductionSettings()
elif deploy == 'DEVELOPMENT':
    config = DevelopmentSettings()
else:
    raise ValueError('Invalid deployment environment: "{}"'.format(deploy))
