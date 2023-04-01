
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.2.

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
SECRET_KEY = '3=m)w@4b%1x7jbosaek8r7$%-4vj370$)=y7b+nig^g002qqdo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000'
# ]
# CORS_ALLOWED_ORIGINS = ["https://mydomain", "http//localhost:3000", "http://127.0.0.1:8000"]

ALLOWED_HOSTS = ['https://selfcare.psst.pt/', 'https://selfcare.psst.pt/api', 'http://127.0.0.1:3000', '127.0.0.1', 'https://development.psst.pt/', 'https://development.psst.pt/api']

CORS_ORIGIN_WHITELIST = (
    'https://selfcare.psst.pt:8000',
    'https://selfcare.psst.pt',
    'https://selfcare.psst.pt/api',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:8000',
    'https://development.psst.pt:8000',
    'https://development.psst.pt',
    'https://development.psst.pt/api'
)

CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: https://selfcare.psst.pt',
    'Access-Control-Allow_origin: https://selfcare.psst.pt.api',
    'Access-Control-Allow-Origin: https://selfcare.psst.pt:8000',
    'Access-Control-Allow-Origin: https://development.psst.pt',
    'Access-Control-Allow_origin: https://development.psst.pt.api',
    'Access-Control-Allow-Origin: https://development.psst.pt:8000',
    'Access-Control-Allow-Origin: http://127.0.0.1:3000',
    'Access-Control-Allow-Origin: http://127.0.0.1:8000',
)
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'crispy_forms',
    'mysite.core',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'mysite/templates'),
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

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {  
    'default': {  
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME': 'rewire',  
        'USER': 'root',  
        'PASSWORD': '',
        'HOST': '127.0.0.1',  
        'PORT': '3306'
    }  
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


PASSWORD_HASHERS = [
  'django.contrib.auth.hashers.PBKDF2PasswordHasher',
  'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
  'django.contrib.auth.hashers.Argon2PasswordHasher',
  'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
  'django.contrib.auth.hashers.BCryptPasswordHasher',
  'django.contrib.auth.hashers.SHA1PasswordHasher',
  'django.contrib.auth.hashers.MD5PasswordHasher',
  'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
  'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
  'django.contrib.auth.hashers.CryptPasswordHasher',
]

# Internationalization

# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/api/static/'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

GSUITE_CREDENTIALS_FILE="file.json"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "m.psst.pt"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "development@m.psst.pt"
EMAIL_HOST_PASSWORD = "development"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/api/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SITE DOMAIN
DOMAIN = "https://selfcare.psst.pt"

# HELLOSIGN DATA
SIGN_CLIENT_EMAIL = 'tigertopdev714@gmail.com'
SIGN_CLIENT_NAME = 'Tiger King'
SIGN_ROLE_NAME = 'Client'
API_KEY = '069a60df057b1cd07437950d039da0f03231c4b70fb991be7d83465741a36f50'
CLIENT_ID = '5a0d30946ddbe8c3b34ddd027ee36f2e'
TEMPLATE_ID='d64a20a34c8a4e8b04052d97bae4d2b66aab0ab7'
CUSTOM_DATE = 'CustomDate'
CUSTOM_NAME = 'customFullName'