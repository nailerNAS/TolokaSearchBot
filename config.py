from os import environ

TOKEN = environ.get('TOKEN')

WEBHOOK_HOST = environ.get('HOST')
WEBHOOK_PORT = 443
WEBHOOK_URL_PATH = f'/{TOKEN}/'

WEBAPP_PORT = environ.get('PORT')
