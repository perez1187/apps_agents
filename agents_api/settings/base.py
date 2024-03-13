from pathlib import Path
import environ
import os

from datetime import timedelta

env = environ.Env()

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = ROOT_DIR / "core_apps"

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    "django.contrib.sites",
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [ 
    'storages',
    "corsheaders",
    "rangefilter", # django admin range filter
    "rest_framework",
    "djoser",
    "rest_framework_simplejwt", 
    'drf_spectacular',   
    'import_export',    
]
LOCAL_APPS = [
    "core_apps.users.users",
    "core_apps.users.profiles",   
    "core_apps.results.agents",
    "core_apps.results.reports",     
 ] 

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agents_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [str(APPS_DIR / "templates")],
        'APP_DIRS': True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.tz", 
            ],
        },
    },
]

WSGI_APPLICATION = 'agents_api.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
ADMINS = [("""Perez""", "o.perez1187@gmail.com")]

MANAGERS = ADMINS
CORS_URLS_REGEX = r"^/api/.*$"

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
SITE_ID = 1
ADMIN_URL = "admin/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
AUTH_USER_MODEL = "users.User"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "error",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5    
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Agents API',
    'DESCRIPTION': 'Technical documentation',
    'VERSION': '1.0.0',
    'COMPONENT_SPLIT_REQUEST': True
    # OTHER SETTINGS
}


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
        "JWT",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=999),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=999),
    "SIGNING_KEY":"cTiizH79Hlcnjul35g9WKjFTV6pyZv1Ii0MovafqWzC5uJrUB9I",
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    
}
DJOSER = {
    "LOGIN_FIELD": "username",
    # "USER_CREATE_PASSWORD_RETYPE": True,
    # "USERNAME_CHANGED_EMAIL_CONFIMATION": True,
    # "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    # "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    # "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    # "ACTIVATION_URL": "activate/{uid}/{token}",
    # "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        # "user_create": "core_apps.users.serializers.CreateUserSerializer",
        # "user": "core_apps.users.serializers.UserSerializer",
        # "current_user": "core_apps.users.serializers.UserSerializer",
        # "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}



LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}