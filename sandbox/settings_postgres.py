from settings import *  # noqa

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'oscar_travis',
#        'USER': 'travis',
#        'PASSWORD': '',
#        'HOST': '127.0.0.1',
#        'PORT': '',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'oscar_django',
        'USER': 'postgres',
        'PASSWORD': 'Nutanix/4u!',
        'HOST': '10.4.220.248',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}
