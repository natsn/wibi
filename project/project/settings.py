import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'zzje5!a(=&0cd$#_##uj**a)f3#v66yrt)%k-nu@o4qlp^abh7'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project',
    'rest_framework',
    'django_extensions',
    'pagedown',
)
REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.TokenAuthentication',
   ),
   'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.IsAuthenticated',
   ),
}
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# APPEND_SLASH = False
STATIC_URL = '/static/' #root appears as this url on website
STATIC_ROOT = (os.path.join(BASE_DIR, 'static/wibi/public')) #where static files are put when collected by developer changes
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/wibi/app'),) #where collector looks for static files
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'static/wibi/app'),) #where django looks for templates, so static/wibi/public/wibi/app/index.html
