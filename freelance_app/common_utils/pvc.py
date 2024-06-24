import random
import string
from django.core.mail import send_mail
from django.conf import settings


def get_random_integer(number):
    return ''.join(random.choices(string.digits, k=number))

def send_email(email, title, text):
    send_mail(title, text, settings.EMAIL_HOST_USER, [email])