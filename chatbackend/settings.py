"""
Django settings for chat project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x1_z1ynyjoolnu=k-$rbbg^v1((86_w99o6@@(59%u2rc=f3(#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DEFAULT_FILE_STORAGE = 'chat.models.MyFileSystemStorage'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'channels',
    'myauth',
    'chat',
    'myadmin'
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://localhost:3000'
)


AUTH_USER_MODEL = 'myauth.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', 
]

ROOT_URLCONF = 'chatbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'chatbackend.wsgi.application'
ASGI_APPLICATION = "chatbackend.routing.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chatdb',
        'USER': 'root',
        'PASSWORD': '332191-Aa',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


LOGGING = {
    'version': 1,   # これを設定しないと怒られる
    'disable_existing_loggers': False,
    'formatters': { # 出力フォーマットを文字列形式で指定する
        'all': {    # 出力フォーマットに`all`という名前をつける
            'format': '\t'.join([
                "[%(levelname)s]",
                "asctime:%(asctime)s",
                "module:%(module)s",
                "message:%(message)s",
            ])
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # ログをどこに出すかの設定
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file_general': { 
            'level': 'DEBUG',  # DEBUG以上のログを取り扱うという意味
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/general.log'),
            'formatter': 'all',
            'maxBytes': 1024 * 1024,
            'backupCount': 10,
        },

    },
    'loggers': {  # どんなloggerがあるかを設定する
        'myLogger': { 
            'handlers': ['file_general', 'console'],  # 先述のfile, consoleの設定で出力
            'level': 'DEBUG',
        },
    },
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static_chat/'
STATIC_ROOT = os.path.join(BASE_DIR,'static') # 追加
STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'auth/static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR,'media') # 追加
MEDIA_URL = '/media_chat/' # 追加

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'おぷきた連絡ナビ <opthok-navi@optech-hokkaido.com>'
DEFAULT_CHARSET = 'utf-8'
EMAIL_HOST = 'smtp.lolipop.jp'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'opthok-navi@optech-hokkaido.com'
EMAIL_HOST_PASSWORD = '-Opthok-navi-Optech-4618-'
EMAIL_USE_SSL = True


NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS = True

CRONJOBS = [
    ('0 * * * *', 'django.core.management.call_command', ['notify_new_message_1-hour']),
    ('*/30 * * * *', 'django.core.management.call_command', ['notify_new_message_30-minutes']),
]
