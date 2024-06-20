from django.core.mail import send_mail
from django.conf import settings

def send_email_to():
    subject="This is test mail"
    message="this. is test message"
    from_send=settings.EMAIL_HOST_USER
    recepient_list=['160957@sdmcujire.in']
    send_mail(subject,message, from_send,recepient_list)