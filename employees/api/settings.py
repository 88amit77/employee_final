import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'qwertyui1234567sdfghj'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
	'api.process',
    'corsheaders',
	# 'django_extensions',
	'drf_yasg',
	'storages',
	'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
	# 'compression_middleware.middleware.CompressionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

WSGI_APPLICATION = 'api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'employees',
        'USER': 'postgres',
        'PASSWORD': 'buymore2',
        'HOST': 'buymore2.cegnfd8ehfoc.ap-south-1.rds.amazonaws.com',
        'PORT': '',
    }
}


# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.postgresql_psycopg2',
# 		'NAME': 'bm_employee',
# 		'USER': 'postgres',
# 		'PASSWORD': 'postgres',
# 		'HOST': 'localhost',
# 		'PORT': '5432',
# 	}
# }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
	'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
	'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 20,
	'DEFAULT_FILTER_BACKENDS': (
	    'django_filters.rest_framework.DjangoFilterBackend',
		),
}

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

STATIC_URL = '/employee/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

CORS_ORIGIN_ALLOW_ALL = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# Dropbox storage
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = 'd7ElXR2Sr-AAAAAAAAAAC2HC0qc45ss1TYhRYB4Jy6__NJU1jjGiffP7LlP_2rrf'
DROPBOX_ROOT_PATH = '/buymore2/'