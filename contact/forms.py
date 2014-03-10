from django import forms
from django.core.mail import send_mail
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
        # send email using the self.cleaned_data dictionary
        send_mail(
            subject='Website Contact Form',
            message=self.format_email(form_data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['josephbkahn@gmail.com'],
            fail_silently=False
        )

    def format_email(self, data):
       return "Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nDate: {date}\nHead Count: {head_count}\nLocation: {location}\nAdditional Information: {additional_info}".format(**data)
