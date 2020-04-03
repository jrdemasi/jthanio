from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'OPTIONS': {
            'read_default_file': os.path.join(os.path.expanduser('~'), '.my.cnf'),
         }
     }
 }

