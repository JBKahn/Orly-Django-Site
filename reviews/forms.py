from django.forms import ModelForm
from reviews.models import ClientReview

from django.core.mail import send_mail
from django.conf import settings


class ClientReviewForm(ModelForm):
    class Meta:
        model = ClientReview
        fields = ['name', 'text']

    def send_email(self):
        form_data = self.cleaned_data
        # send email using the self.cleaned_data dictionary
        send_mail('Website Review added from ' + form_data.get('name'), form_data.get('text'), settings.EMAIL_HOST_USER, ['josephbkahn@gmail.com'], fail_silently=False)
