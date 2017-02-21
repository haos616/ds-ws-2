from celery import shared_task
from celery.contrib import rdb

from django.core.mail import send_mail


@shared_task
def hello():
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
