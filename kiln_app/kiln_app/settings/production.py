
import os
from .settings import *


ALLOWED_HOSTS = ['kiln-app.herokuapp.com', 'localhost', '127.0.0.1']

# remeber to set this enviromental variable in you production server
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    '^8ai-6gb)yyg19uangdahsi8a%c=)mb0yler7%0jlh1mz!^gnago;91_')

DEBUG = False
