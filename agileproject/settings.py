"""
Django settings for agileproject project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lq*$5ez16@j7^c$cmkd5jj9x)-tulf!abdvwtr^nd7*%it@b0q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'home',
    'account',
    'account_settings',
    'invite_user',
    'user_story_view',
    'manage_product',
    'manage_team',
    'manage_epic_capability',
    'manage_features',
    'helpuser',
    'manage_backlogs',
    'manage_iterations',
    'import_export',
    # 'product_view',
    # 'backlog_view',
    'manage_user_profile',
    'manage_role',
    'user_story_points',
    'manage_team_member',
    'feedback',
    'manage_goals',
    'manage_benefits',
    'data_import_export',
    # ---------------------------
    'business_value',
    'ar_scenario',
    'manage_jobmot_set',
    'manage_joboutc_set',
    'manage_jobsit_set',
    'manage_testact_set',
    'manage_testcond_set',
    'manage_testoutc_set',
    'job_story_view',
    'test_story_view',
    'words_and_patterns',
    'user_story_value',
    'feature_value',


    # -----------------------
    'subscription',
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

ROOT_URLCONF = 'agileproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                TEMPLATES_DIR,
        ],
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

WSGI_APPLICATION = 'agileproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     # }

#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # Database Engine of PostgreSQL Database
#         'NAME': 'agile_database',  # Database Name
#         'USER': 'root',  # Database has a Root User
#         'PASSWORD': 'Digimonk@123',  # Database Connection Password
#         'HOST': "",  # IP Address for Localhost
#         'PORT' : "",
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_ROOT = "/home/user/agileready/static"
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    STATIC_DIR

]

BASE_URL = 'http://digimonk.co/'
# BASE_URL = 'http://3.20.218.126/'
# BASE_URL = 'https://beagileready.com/'

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL ='/media/'


LOGIN_REDIRECT_URL = '/superadmin/'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail.agileready.net'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER = 'customercare@agileready.net'
# EMAIL_HOST_PASSWORD = 'We@care2020&'
EMAIL_HOST_USER = 'praveen.vaidhya@digimonk.in'
EMAIL_HOST_PASSWORD = '8871006808'






SASS_PROCESSOR_ENABLED = True

X_FRAME_OPTIONS = 'SAMEORIGIN https://beagileready.com/'