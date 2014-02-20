from django import forms
from django.core.mail import send_mail
from django.conf import settings
from localflavor.ca import forms as CAFormFields


class ContactForm(forms.Form):
    email_address = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone_number = CAFormFields.CAPhoneNumberField()
    ext = forms.IntegerField()
    message = forms.CharField()

    def send_email(self):
        form_data = self.cleaned_data
        # send email using the self.cleaned_data dictionary
        send_mail('Website Contact Form from ' + form_data.get('first_name') + ' ' + form_data.get('last_name') + ' ' + form_data.get('phone_number') + " " + form_data.get('email_address'), form_data.get('message'), settings.EMAIL_HOST_USER, ['josephbkahn@gmail.com'], fail_silently=False)
