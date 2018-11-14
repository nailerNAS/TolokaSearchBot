from os import environ

TOKEN = environ.get('TOKEN')

WEBHOOK_HOST = environ.get('HOST')
WEBHOOK_PORT = 443
WEBHOOK_URL_PATH = f'/{TOKEN}/'
WEBHOOK_URL = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_URL_PATH}'

WEBAPP_PORT = environ.get('PORT')
