import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'env_sync.settings')

app = Celery('env_sync')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

