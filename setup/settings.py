import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = os.path.join('./', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a+*_zq0m)h75#lrgy8_jkl)7c(rrre11ffc4&mlmfd^8qxisg3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "292bb9fed781.ngrok-free.app"
]

CSRF_TRUSTED_ORIGINS = [
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # MyApp
    'autenticacao.apps.AutenticacaoConfig',
    'usuarios.apps.UsuariosConfig',
    'whatsapp.apps.WhatsappConfig',
    'dashboard.apps.DashboardConfig',
    'broadcasts.apps.BroadcastsConfig',
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

ROOT_URLCONF = 'setup.urls'

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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['DB_NAME'],        
#         'USER': os.environ['DB_USER'],           
#         'PASSWORD': os.environ['DB_PASSWORD'],          
#         'HOST': os.environ['DB_HOST'],               
#         'PORT': os.environ['DB_PORT'],                 
#     }
# }
CSRF_TRUSTED_ORIGINS = [
    "https://292bb9fed781.ngrok-free.app",
]



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'autenticacao.backends.UsernameOrEmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'usuarios.Usuario'

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'setup/static'),]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'handlers': ['console', 'file'], # ['console', 'file']
            'level': 'DEBUG',

        },
        'celery': {  # Desabilita o Celery
            'handlers': [],
            'level': 'ERROR',  # Só registra erros graves
            'propagate': False,
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join('./', 'logs', 'logs.log'),
            'formatter': 'simple',
        },
        'console': {
           'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'formatters': {
        'simple': {
            'format': '{asctime} - {levelname} - {name}:{lineno} - {message}',
            'style': '{',
        },
    },
}
