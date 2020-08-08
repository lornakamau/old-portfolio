from django import forms

class ContactForm(forms.Form):
    sender_name = forms.CharField(required=True, label = "Your name")
    sender_email = forms.EmailField(required=True, label = "Your email address")
    message = forms.CharField(widget=forms.Textarea, required=True, label = "Your message")