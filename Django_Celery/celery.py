import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Celery.settings')
app = Celery('Django_Celery')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'Asia/Tashkent'

app.conf.beat_schedule = {
    "every_thirty_seconds": {
        "task": "users.tasks.thirty_second_func",
        "schedule": timedelta(seconds=30),
    },
}

app.autodiscover_tasks()

