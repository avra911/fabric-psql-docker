from fabric_bolt.core.settings.base import *

DEBUG = True

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Asia/Yekaterinburg'
CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# Remeber to set the SECRET_KEY environment variable when putting this into
# production so no one can spoofe your sessions. Changing this will cause your
# current user sessions to become invalidated.
SECRET_KEY = os.environ.get('SECRET_KEY') or 'notasecret'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'mail.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'login@gmail.ru'
# EMAIL_HOST_PASSWORD = 'password'
