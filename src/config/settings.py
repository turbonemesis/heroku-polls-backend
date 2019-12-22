"""
Django settings for Heroku Polls sample project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False), )
env.read_env(env_file=root('.env'))

BASE_DIR = root()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])


LOCAL = [
    'django_extensions',
]

PRODUCTION = [
    'django_s3_storage',
]

COMMON = [
    'rest_framework',
    'corsheaders',
]

APPS = [
	'polls.apps.PollsConfig',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + COMMON + APPS

if DEBUG:
    INSTALLED_APPS += LOCAL

if not DEBUG:
    INSTALLED_APPS += PRODUCTION


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': env.db(default='postgres://postgres:postgres@db:5432/postgres',)
}

# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'polls',
#             'USER': 'polls',
#             'PASSWORD': 'test1234',
#             'HOST': 'localhost',
#             # 'PORT': '19089'
#         }
#     }


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}


CORS_ORIGIN_ALLOW_ALL = True


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


if not DEBUG:
    DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
    STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'
    AWS_REGION = env('AWS_REGION')
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_S3_BUCKET_NAME_STATIC = env('AWS_S3_BUCKET_NAME_STATIC')
    AWS_S3_BUCKET_AUTH_STATIC = False

STATIC_URL = '/static/'
STATIC_ROOT = (root - 1)('static')

MEDIA_URL = '/media/'
MEDIA_ROOT = (root - 1)('media')
