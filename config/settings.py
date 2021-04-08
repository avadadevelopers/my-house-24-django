import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_ROOT = Path(__file__).resolve(strict=True).parent

SECRET_KEY = 'n+3wtig^!b(&ytgzr7f5wvs-_g*_&@@84kn5+u3ygjzv3+8kp^'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    '_db.apps.DbConfig',
    'app_public.apps.PublicConfig',
    'app_admin.apps.AdminConfig',
    'app_cabinet.apps.CabinetConfig',
    'crispy_forms',
    'easy_maps',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = '_db.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'app_admin.middleware.AccessCheckMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

AUTHENTICATION_BACKENDS = [
    '_db.auth.EmailAuthBackend'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        #############################################################################
        # Make sure postgres is installed on your local machine before uncommenting #
        #############################################################################
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'MyHouse24',
        # 'USER': 'MyHouse24',
        # 'PASSWORD': 'MyHouse24',
        # 'HOST': '127.0.0.1',
        # 'PORT': '5432',
    }
}

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

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

EASY_MAPS_GOOGLE_KEY = 'AIzaSyAMPq6gbs7dfX-AMgFtCvTpjK8ltHErwcY'