from django import forms


class ContactForm(forms.Form):
    email_address = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20)
    message = forms.CharField()
