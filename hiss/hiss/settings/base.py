"""
Django settings for hiss project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "user.apps.UserConfig",
    "application.apps.ApplicationConfig",
    "volunteer.apps.VolunteerConfig",
    "status.apps.StatusConfig",
    "phonenumber_field",
    "customauth.apps.CustomauthConfig",
    "shared.apps.SharedConfig",
    "team.apps.TeamConfig",
    "anymail",
    "django_admin_listfilter_dropdown",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hiss.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "..", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "shared.context_processors.customization",
            ]
        },
    }
]

WSGI_APPLICATION = "hiss.wsgi.application"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "US/Central"

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = "resumes/"
MEDIA_URL = "/resumes/"
MAX_UPLOAD_SIZE = "10485760"
LOGIN_REDIRECT_URL = reverse_lazy("status")
LOGOUT_REDIRECT_URL = reverse_lazy("customauth:login")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "..", "static/")]
STATIC_ROOT = "public/"
APPEND_SLASH = True
AUTH_USER_MODEL = "user.User"

# TODO(SaltyQuetzals): Remove http://localhost:3000 for day-of
CORS_ORIGIN_WHITELIST = [
    "https://volunteer.tamuhack.com",
    "https://tamuhack-org.github.io",
    "http://localhost:3000",
]

CORS_URLS_REGEX = r"^/api/.*$"
