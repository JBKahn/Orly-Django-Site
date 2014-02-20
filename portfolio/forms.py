from django import forms


class PortfolioForm(forms.Form):
    imgfile = forms.FileField(
        label='Select an Image'
    )
