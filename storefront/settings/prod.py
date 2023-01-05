from .common import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['jamie-storefront-prod.herokuapp.com']

DATABASE_URL = os.environ['JAWSDB_URL']

database_attr = DATABASE_URL.split(':')

JaName = database_attr[3].split('/')[1].rstrip("'")
JaUser = database_attr[1].lstrip('//')
JaPwrd = database_attr[2].split('@')[0]
JaHost = database_attr[2].split('@')[1]
JaPort = int(database_attr[3].split('/')[0])

DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': JaName,
        'USER': JaUser,
        'PASSWORD': JaPwrd,
        'HOST': JaHost,
    }
}

REDIS_URL = os.environ['REDISCLOUD_URL']

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "TIMEOUT": 60 * 10,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
DEFAULT_FROM_EMAIL = 'test@store.com'