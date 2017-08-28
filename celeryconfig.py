# config file for Celery Daemon

DJANGO_SETTINGS_MODULE='projectanka.settings'

# default RabbitMQ broker
BROKER_URL = 'amqp://'

# default RabbitMQ backend
CELERY_RESULT_BACKEND = 'amqp://'