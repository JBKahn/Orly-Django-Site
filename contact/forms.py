from django import forms
from django.core.mail import EmailMessage
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=40, required=False)
    date = forms.DateField(required=False)
    head_count = forms.IntegerField(min_value=0, max_value=500, required=False)
    location = forms.CharField(max_length=100, required=False)
    additional_info = forms.CharField(required=False)

    def send_email(self):
        form_data = self.cleaned_data
        email = EmailMessage(
            subject='Website Contact Form from {}'.format(form_data.get('name')),
            body=self.format_email(form_data),
            from_email=settings.EMAIL_HOST_USER,
            to=['orly@orlywaldman.com'],
            headers={'Reply-To': form_data.get('email')}
        )
        email.send(fail_silently=False)

    def format_email(self, data):
        return "Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nDate: {date}\nHead Count: {head_count}\nLocation: {location}\nAdditional Information: {additional_info}".format(**data)


class JBKahnContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)

    def send_email(self):
        form_data = self.cleaned_data
        email = EmailMessage(
            subject='Website Contact Form from {}'.format(form_data.get('name')),
            body=self.format_email(form_data),
            from_email=settings.EMAIL_HOST_USER,
            to=['josephbkahn@gmail.com'],
            headers={'Reply-To': form_data.get('email')}
        )
        email.send(fail_silently=False)

    def format_email(self, data):
        return "Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}".format(**data)
