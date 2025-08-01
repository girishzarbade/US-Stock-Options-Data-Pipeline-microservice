"""
Django settings for data_collector_service project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-k^c404!2*woj(h(+ek*e#=0sh^qrjw9y-g34m^*qy=^=!43v%^')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", "localhost"]


# Application definition

INSTALLED_APPS = [
    "django_prometheus",
    'api_handler',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'corsheaders',
    
]

MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",

]

ROOT_URLCONF = "data_api_service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "data_api_service.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',
#         'NAME': os.getenv('SQL_DATABASE', 'us_stock_options_db'),
#         'OPTIONS': {
#             'driver': os.getenv('SQL_DRIVER', 'ODBC Driver 18 for SQL Server'),
#             'host': os.getenv('SQL_SERVER', 'dash-gtd.database.windows.net'),
#             'database': os.getenv('SQL_DATABASE', 'us_stock_options_db'),
#             'user': os.getenv('SQL_USERNAME', 'dash_gtd'),
#             'password': os.getenv('SQL_PASSWORD', 'wearethebest@69'),
#             'extra_params': 'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=60',
#         },
#     },
#     'secondary_db': {
#         'ENGINE': 'django.db.backends.dummy',
#         'NAME': os.getenv('SQL_DATABASE', 'us_stock_options_db'),
#         'OPTIONS': {
#             'driver': os.getenv('SQL_DRIVER', 'ODBC Driver 18 for SQL Server'),
#             'host': os.getenv('SQL_SERVER', 'dash-gtd.database.windows.net'),
#             'database': os.getenv('SQL_DATABASE', 'us_stock_options_db'),
#             'user': os.getenv('SQL_USERNAME', 'dash_gtd'),
#             'password': os.getenv('SQL_PASSWORD', 'wearethebest@69'),
#             'extra_params': 'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=60',
#         },
#     }
# }

# DATABASE_ROUTERS = ['api_handler.routers.MultiDBRouter']

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#     ]
# }
# ALLOWED_HOSTS = ['*']

# # CORS settings
# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:4200",
#     "http://127.0.0.1:4200",
# ]

# CORS_ALLOW_METHODS = [
#     'GET',
#     'POST',
#     'PUT',
#     'DELETE',
#     'OPTIONS'
# ]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'us_stock_options_db'),
        'USER': os.getenv('POSTGRES_USER', 'sa'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'Passw0rd!'),
        'HOST': os.getenv('POSTGRES_HOST', 'postgres'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#     ]
# }
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'JSON_ENCODER': 'api_handler.views.CustomJSONEncoder',
}

ALLOWED_HOSTS = ['*']

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'OPTIONS'
]