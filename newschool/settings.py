"""
Django settings for newschool project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
PROJECT_ROOT = os.path.dirname(__file__)
PROJECT_PATH = os.path.dirname(PROJECT_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uhkr8+k-i^4y9yzmxowzglu%$t_0vovtp8!4h85lol09%xeidk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'roster',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'newschool.urls'

WSGI_APPLICATION = 'newschool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'newschool.db'), # Add 'postgresql_psycopg2', 'mysql'
        'USER': '',                        # Not used with sqlite3
        'PASSWORD': '',                    # Not used with sqlite3
        'HOST': '',                        # Set to empty string for localhost. Not used with sqlite3
        'PORT': '',                        # Set to empty string for localhost. Not used with sqlite3
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# Absolute filesystem path to the directory that will hold user-uploaded files
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media_root')


#URL that handles the media served from MEDIA_ROOT. Make sure to use a trailing slash.
MEDIA_URL = '/media/'


#Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static_media')


# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static_media'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

