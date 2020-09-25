from account.models import Ar_user,AR_organization
from django import forms

class accountform(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
    State = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
    Zip = forms.CharField(widget=forms.NumberInput(),required=True,max_length=12)
    Country = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
    Phone = forms.CharField(widget=forms.NumberInput(),required=True,max_length=12)


