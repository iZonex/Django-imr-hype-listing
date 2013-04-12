# Django settings for imr project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.orkut.OrkutBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TWITTER_CONSUMER_KEY         = 'YOst2ufrGQ3LKssnT0bnYw'
TWITTER_CONSUMER_SECRET      = '54FEKcYxk1rQRTOt4agcRS6hxMBYjvAtgmeCTQ2hN8A'
#FACEBOOK_APP_ID              = ''
#FACEBOOK_API_SECRET          = ''
#LINKEDIN_CONSUMER_KEY        = ''
#LINKEDIN_CONSUMER_SECRET     = ''
#ORKUT_CONSUMER_KEY           = ''
#ORKUT_CONSUMER_SECRET        = ''
#GOOGLE_CONSUMER_KEY          = ''
#GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = '606140149231.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'KQLNoGbDxlJ6qt38IXG5arxo'
#FOURSQUARE_CONSUMER_KEY      = ''
#FOURSQUARE_CONSUMER_SECRET   = ''
#VK_APP_ID                    = ''
#VK_API_SECRET                = ''
#LIVE_CLIENT_ID               = ''
#LIVE_CLIENT_SECRET           = ''
#SKYROCK_CONSUMER_KEY         = ''
#SKYROCK_CONSUMER_SECRET      = ''
#YAHOO_CONSUMER_KEY           = ''
#YAHOO_CONSUMER_SECRET        = ''

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
# Django Registration
ACCOUNT_ACTIVATION_DAYS = 2

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'info@inmoneyrise.com'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', #'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'imr',                      # Or path to database file if using sqlite3.
        'USER': 'zonex',                      # Not used with sqlite3.
        'PASSWORD': '0lvbyr0',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/zonex/www/imr/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/zonex/www/imr/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
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

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4m^nk8g-&amp;3$itb@lub$967g6!y9&amp;hql(rvhkhx^-(=i)t%%t#n'

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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

ROOT_URLCONF = 'imr.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'imr.wsgi.application'

TEMPLATE_DIRS = (
    #'/home/zonex/www/imr/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth'
#    'social_auth.context_processors.social_auth_by_name_backends',
#    'social_auth.context_processors.social_auth_backends',
#    'social_auth.context_processors.social_auth_by_type_backends',
#    'social_auth.context_processors.social_auth_login_redirect',
#)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'listing',
    'imperavi',
    'south',
    'modeltranslation',
    'news',
    'registration',
    'customuseradmin',
    'social_auth'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
