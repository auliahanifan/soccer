"""
Django settings for soccerapi project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'secretKey')


USE_CACHE = (os.environ.get('USE_CACHE') == 'true')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '*o7e(@zt#&cs9h2$)jp7lrg_=$wy(hhf&9ftb-khh5r2d%1ys='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'rest_framework',
    'drf_yasg',
    'django_extensions', # $ python manage.py show_urls
    'django_nose',

    # Our app
    'team',

]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-html',
    '--cover-package=team',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }

ROOT_URLCONF = 'soccerapi.urls'

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

WSGI_APPLICATION = 'soccerapi.wsgi.application'

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://localhost:6379/',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }


SQLITE_CONFIG = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

PG_DB_NAME = os.environ.get('PG_DB_NAME', 'postgres')
PG_USERNAME = os.environ.get('PG_USERNAME', 'postgres')
PG_PASSWORD = os.environ.get('PG_PASSWORD', '')
PG_HOST = os.environ.get('PG_HOST', 'localhost')
PG_PORT = os.environ.get('PG_PORT', '5432')

USE_POSTGRES = (os.environ.get('USE_POSTGRES', '') == 'true')

POSTGRES_CONFIG = {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': PG_DB_NAME,

        'USER': PG_USERNAME,

        'PASSWORD': PG_PASSWORD,

        'HOST': PG_HOST,

        'PORT': PG_PORT,

    }

DATABASES = {
    'default': POSTGRES_CONFIG if USE_POSTGRES else SQLITE_CONFIG
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# TEMPLATE_PATH = os.path.join(BASE_DIR, 'cover')
# STATIC_PATH = os.path.join(BASE_DIR, 'cover')
# STATIC_ROOT = os.path.join(BASE_DIR, 'cover')
# STATIC_URL = os.path.join(BASE_DIR,'/cover/')
STATIC_URL = '/test-result/'
# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates'),
# )
STATICFILES_DIRS = [
    BASE_DIR / "cover",
    # '/var/www/static/',
]

