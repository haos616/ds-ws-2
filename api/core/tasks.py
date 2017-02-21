from celery import shared_task
from celery.contrib import rdb


@shared_task
def hello():
    rdb.set_trace()
    print('Hello')
