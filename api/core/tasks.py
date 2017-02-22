from django.core.mail import send_mail

from celery_app import app as celery_app


@celery_app.task
def hello():
    send_mail(
        'Subject here 2',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
