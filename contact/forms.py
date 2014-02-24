from django import forms
from django.core.mail import send_mail
from django.conf import settings
from localflavor.ca import forms as CAFormFields


class ContactForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20)
    message = forms.CharField()

    def send_email(self):
        form_data = self.cleaned_data
        # send email using the self.cleaned_data dictionary
        send_mail(
            subject='Website Contact Form',
            message=self.format_email(form_data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['josephbkahn@gmail.com'],
            fail_silently=False
        )

    def format_email(self, data):
       return "Name: {first_name} {last_name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}".format(**data)
