from django import forms
from django import forms

class AddressForm(forms.Form):
    street = forms.CharField(label="street", max_length=255)
    city = forms.CharField(label="city", max_length=255)
    province = forms.CharField(label="province", max_length=255)
    postal = forms.CharField(label="postal", max_length=50)