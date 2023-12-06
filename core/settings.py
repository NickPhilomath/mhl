from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# useful functions

def get_list(text):
    return [item.strip() for item in text.split(",")]


# def get_bool_from_env(name, default_value):
#     if name in os.environ:
#         value = os.environ[name]
#         try:
#             return ast.literal_eval(value)
#         except ValueError as e:
#             raise ValueError(f"{value} is an invalid value for {name}") from e
#     return default_value


# def get_url_from_env(name, *, schemes=None) -> Optional[str]:
#     if name in os.environ:
#         value = os.environ[name]
#         message = f"{value} is an invalid value for {name}"
#         URLValidator(schemes=schemes, message=message)(value)
#         return value
#     return None

# setting up some constants
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
SAMSARA_API_KEYS = get_list(os.getenv('SAMSARA_API_KEYS'))
OWM_API_KEY = os.getenv('OWM_API_KEY')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE_NAME = os.getenv('MYSQL_DATABASE_NAME')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'api'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'public'
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database

DATABASES = {
    'default': {
        # default
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        # mysql
        # 'ENGINE': 'django.db.backends.mysql',
        # 'HOST': 'localhost',
        # 'NAME': MYSQL_DATABASE_NAME,
        # 'USER': MYSQL_USER,
        # 'PASSWORD': MYSQL_PASSWORD,
    }
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# restframework
REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
   'ACCESS_TOKEN_LIFETIME': timedelta(minutes=2)
}

# AUTH_USER_MODEL = 'core.User'

# DJOSER = {
#     'SERIALIZERS': {
#         'user_create': 'core.serializers.UserCreateSerializer',
#         'user': 'core.serializers.UserSerializer',
#         'current_user': 'core.serializers.UserSerializer',
#     }
# }

# cors settings
CORS_ALLOWED_ORIGINS  = [
    "http://localhost:3000", # react host
    "http://127.0.0.1:3000", # react host
]
# CORS_ALLOW_ALL_ORIGINS = True

#debug toolbar settings
INTERNAL_IPS = [
    '127.0.0.1'
]

# # celery settings
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1' # /1

CELERY_BEAT_SCHEDULE = {
    # 'notifyCustomers': {
    #     'task': 'api.tasks.notify_customers',
    #     'schedule': 5, # every five seconds
    #     # 'schedule': crontab(minute='*/15') # every 15 minutes
    #     # 'schedule': crontab(day_of_week=1, hour=7, minute=30) # every monday at 7:30 am
    #     'args': ['hello world'],
    # },
    'update_trucks': {
        'task': 'api.tasks.update_trucks',
        'schedule': 5 * 60,
    },
    # 'logTrailers': {
    #     'task': 'api.tasks.log_trailers',
    #     'schedule': 2 * 60
    # }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# GRAPHENE = {
#     "SCHEMA": "api.schema.schema"
# }

# HTTPS settings
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# HSTS settings
# SECURE_HSTS_SECONDS = 31536000 # 1 year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True