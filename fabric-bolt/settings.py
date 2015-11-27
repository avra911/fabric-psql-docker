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

TIME_ZONE = 'Asia/Yekaterinburg'

LANGUAGE_CODE = 'ru-RU'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'mail.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'login@gmail.ru'
# EMAIL_HOST_PASSWORD = 'password'
