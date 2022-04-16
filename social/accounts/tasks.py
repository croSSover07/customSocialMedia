import logging

from django.urls import reverse
from django.core.mail import send_mail, get_connection
from django.contrib.auth import get_user_model

from social.celery import app


@app.task
def send_information_email(email):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.filter(email=email).first()
        connect = get_connection()
        send_mail(
            'Information about new account',
            f'You have registered new acc:{user}',
            'from@customasocialmedia.dev',
            [email],
            fail_silently=False,
            connection=connect
        )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % email)