from django.shortcuts import render
from django.conf import settings
from .models import Project
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMessage
from .forms import ContactForm
from django.contrib import messages
from .email import send_email
from django.http import JsonResponse
from django.template.loader import render_to_string

def home(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, per_page=6)
    page_number = request.GET.get('page', 1)
    page_object = paginator.get_page(page_number)
    form = ContactForm()
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = request.POST.get('sender_name')
            sender_email = request.POST.get('sender_email')
            message = request.POST.get('message')
            name = sender_name.title()
            email_name = sender_name.upper()
            send_email(email_name, message, send_email)
            data = {'Success': f'Dear {name}, thank you for your message. Your email has been sent successfully! I shall get back to you shortly.'}

            email_template = render_to_string('email/confirmation.html', {'name': name})
            email = EmailMessage(
                'Thank you for contacting Wanjiru Kamau',
                email_template,
                settings.EMAIL_HOST_USER,
                [sender_email],        
            )
            email.fail_silently = False
            email.send()
            return JsonResponse(data)

    return render(request, 'home.html', {"projects": page_object, "paginator": paginator, "page_number": int(page_number), "ContactForm": form})

