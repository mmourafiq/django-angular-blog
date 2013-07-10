# Django settings for tipstry project.
import os.path
import posixpath
from local_settings import *

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
# here is all the languages supported by the CMS
#gettext_noop = lambda s: s
#PAGE_LANGUAGES = (
#    ('fr-fr', gettext_noop('french')),
#)

SITE_ID = 1
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',    
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',    
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    TEMPLATE_ROOT,    
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.request',
   'django.core.context_processors.static',
   'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',    
    'django.middleware.locale.LocaleMiddleware',    
    'django.middleware.clickjacking.XFrameOptionsMiddleware',        
)

#variables for registration
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; 
LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'blog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'blog.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',                                 
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

#importing envirment --dev or prod-- local variables
if DEV_ENV:
    from dev_settings import *
    MIDDLEWARE_CLASSES += DEV_MIDDLEWARE_CLASSES
    INSTALLED_APPS += DEV_INSTALLED_APPS
    TEMPLATE_CONTEXT_PROCESSORS += DEV_TEMPLATE_CONTEXT_PROCESSORS

if PROD_ENV:
    from prod_settings import *
    MIDDLEWARE_CLASSES += PROD_MIDDLEWARE_CLASSES
    INSTALLED_APPS += PROD_INSTALLED_APPS
    TEMPLATE_CONTEXT_PROCESSORS += PROD_TEMPLATE_CONTEXT_PROCESSORS   