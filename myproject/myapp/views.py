from django.shortcuts import redirect, render
from .utils import send_email_to
# Create your views here.
def home(req):
    send_email_to()
    return redirect("/")