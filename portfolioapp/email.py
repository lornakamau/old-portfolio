from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(name, message, sender):
    # Creating message subject and sender
    subject = f'WORK PROPOSAL FROM {name}'
    receiver = 'lornadeveloper@gmail.com'
    
    #passing in the context vairables
    text_content = render_to_string('email/email.txt',{"message":message})
    html_content = render_to_string('email/email.html',{"message":message})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()