# Django settings for webapp project.
import os
import json

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Open Science Data', 'opendata.science@gmail.com')
)

MANAGERS = ADMINS

try:
    env = json.load(open('/home/dotcloud/environment.json'))
except IOError:
    env = {
        'DOTCLOUD_DB_SQL_LOGIN':'',
        'DOTCLOUD_DB_SQL_PASSWORD':'',
        'DOTCLOUD_DB_SQL_HOST':'',
        'DOTCLOUD_DB_SQL_PORT':0,
    }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'template1',
        'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DB_SQL_HOST'],
        'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
    }
}

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

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/dotcloud/data/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/dotcloud/data/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://www.opensciencedata.org/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'r_hi5c3^(&%l@lmmk)f^clqj%k&5!ie)7a0&s)sa#u5380l9-h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'webapp.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
    os.path.join(os.path.dirname(__file__), 'templates', 'datasets'),
    os.path.join(os.path.dirname(__file__), 'templates', 'users'),
    os.path.join(os.path.dirname(__file__), 'templates', 'tags'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',
    # 'django.contrib.admindocs',
    'webapp.datasets',
    'webapp.tags',
    'webapp.users',
    'tagging',
    'userena',
    'guardian',
    'easy_thumbnails',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
ANONYMOUS_USER_ID = -1
USERENA_MUGSHOT_DEFAULT = 'monsterid'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
AUTH_PROFILE_MODULE = 'users.UserProfile'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
LOGIN_REDIRECT_URL = '/'
USERENA_SIGNIN_REDIRECT_URL = '/'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
FORCE_LOWERCASE_TAGS = True

from secure_settings import *
