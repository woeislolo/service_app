import os

from dotenv import dotenv_values

from .base import *


print('local')

config = dotenv_values()
SECRET_KEY = config.get('DJANGO_SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.get('POSTGRES_DB'),
        "USER": config.get("POSTGRES_USER"),
        "PASSWORD": config.get("POSTGRES_PASSWORD"),
        "HOST": config.get("POSTGRES_HOST"),
        "PORT": config.get("POSTGRES_PORT"),
    },
}

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'formatter':{
            'format': '{levelname} {asctime} {filename} {message}',
            'style': '{', 
            },
        },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            # 'formatter': 'formatter',
            # 'encoding': 'UTF-8'
            },
        },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console',],
            'level': 'DEBUG',
        }
    }
}
