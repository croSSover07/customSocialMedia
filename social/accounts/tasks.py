import logging

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from social.celery import app


@app.task
def send_information_email(email):
    print('send_information_email')
    UserModel = get_user_model()
    try:
        user = UserModel.objects.filter(email=email).first()
        send_mail(
            'Information about new account',
            f'You have registered new acc:{user}',
            # 'http://localhost:8000%s' % reverse('verify', kwargs={'email': str(email)}),
            # 'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            'from@customasocialmedia.dev',
            [email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % email)