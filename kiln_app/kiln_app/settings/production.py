
import os
from .settings import *


ALLOWED_HOSTS = ['kiln-app.herokuapp.com', 'localhost', '127.0.0.1']

# remember to set this enviromental variable in you production server
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    '^8ai-6gb)yyg19uangdahsi8a%c=)mb0yler7%0jlh1mz!^gnago;91_')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dmtltpue5kc80',
        'USER': 'vaplgmvzyhxcne',
        'PASSWORD': 'c5b644607d8acde39a3f000ee438965ed994a71da2d371fe851c5912462c61f5',
        'HOST': 'ec2-50-19-254-63.compute-1.amazonaws.com',
        'PORT': '5432',
        'URI': 'postgres://vaplgmvzyhxcne:c5b644607d8acde39a3f000ee438965ed994a71da2d371fe851c5912462c61f5@ec2-50-19-254-63.compute-1.amazonaws.com:5432/dmtltpue5kc80'
    }
}
# overwriting the basic settings
DEBUG = True
