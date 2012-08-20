# Django settings for pyweek project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = []

MANAGERS = ADMINS

DATABASES = {}

# Absolute path to the directory that holds media.
MEDIA_ROOT = '/home/pyweek/media/dl/'

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = 'http://media.pyweek.org/dl/'

# Path to the two RSS files generated by the challenge diary RSS generation
# code
DIARY_RSS_FILE_NEW = '/home/pyweek/media/rss/diaries.rss.new'
DIARY_RSS_FILE = '/home/pyweek/media/rss/diaries.rss'

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC' #America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'pyweek.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    '/home/pyweek/lib/pyweek/challenge/templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.contrib.messages.context_processors.messages",
#    "django.core.context_processors.i18n",
    "pyweek.challenge.views.context.challenges",
)

STATIC_ROOT = '/home/pyweek/static/'
STATIC_URL = 'http://pyweek.org/static/'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'pyweek.challenge',
    'django_wysiwyg',
]

try:
    import raven
    INSTALLED_APPS.append('raven.contrib.django')
except ImportError:
    pass

# now load local modifications to these settings
import os
with open(os.environ['DJANGO_LOCAL_SETTINGS']) as f:
    exec f

