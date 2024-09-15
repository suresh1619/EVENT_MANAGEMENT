# views.py

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django import forms
import datetime

# Define the form within the view
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Email content
            html_message = render_to_string('send_email.html', {
                'name': name,
                'message': message,
                'current_year': datetime.datetime.now().year,
            })
            plain_message = strip_tags(html_message)

            # Sending the email
            email_message = EmailMessage(
                subject,
                plain_message,
                email,  # Sender
                ['clopileta8@gmail.com'],  # List of recipients
            )
            email_message.content_subtype = 'html'
            email_message.send()

            messages.success(request, 'Your email has been sent successfully!')
            return redirect('send_email')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
