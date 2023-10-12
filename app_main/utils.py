from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.template.loader import render_to_string


def send_owner_query_mail(obj,client_name, client_email):
    subject = 'New Product Query'
    c = {
        'product_id':obj.id,
        'product_title':obj.title,
        'client_name': client_name,
        'client_email': client_email,
    }
    text_version = 'email-templates/owner-query-email.txt'
    text_message = render_to_string(text_version,c)

    try:
        send_mail(subject, text_message, settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_OWNER_MAIL])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    

def send_client_query_mail(obj,client_name, client_email):
    subject = 'New Product Query'
    c = {
        'product_id':obj.id,
        'product_title':obj.title,
        'client_name': client_name,
        'client_email': client_email,
    }
    text_version = 'email-templates/client-query-email.txt'
    text_message = render_to_string(text_version,c)

    try:
        send_mail(subject, text_message, settings.DEFAULT_FROM_EMAIL,[client_email])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    

def send_owner_contact_mail(client_name, client_email,client_message):
    subject = 'New Contact Form Submission'
    c = {
        'client_name': client_name,
        'client_email': client_email,
        'client_message': client_message,
    }
    text_version = 'email-templates/owner-contact-email.txt'
    text_message = render_to_string(text_version,c)

    try:
        send_mail(subject, text_message, settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_OWNER_MAIL])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    

def send_client_contact_mail(obj,client_name, client_email,client_message):
    subject = 'Response to Your Contact Form Submission'
    c = {
        'contact':obj,
        'client_name': client_name,
        'client_email': client_email,
        'client_message': client_message,
    }
    text_version = 'email-templates/client-contact-email.txt'
    text_message = render_to_string(text_version,c)

    try:
        send_mail(subject, text_message, settings.DEFAULT_FROM_EMAIL,[client_email])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    