from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9srw+1#cgl)m&_m&3t&q_dg*8o2ctn9&d2ibv7%$+%hcr5%153'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'backend',
        'HOST' : 'localhost',#docker
        'USER' : 'root',
        'PASSWORD' : 'spartaamir12342002'
    }
}