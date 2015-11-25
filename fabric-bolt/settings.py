from fabric_bolt.core.settings.base import *

DEBUG = True

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fabric',
        'USER': 'fabric',
        'PASSWORD': '5aL9deW8uP32',
        'HOST': 'pgsqldb',
        'PORT': '5432',
    }
}

SECRET_KEY = 'e1rCEoBwnGnsXGSN2Xw1XMJMLlNALLk8KaQQCglUo/5o5fEcMTLP3Q=='
