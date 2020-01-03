from django.forms import forms
from django.contrib.auth.models import User
from .models import Ar_user

class UserAuth(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')

class Ar_user(forms.ModelForm):
    class Meta:
        model = Ar_user
        fields = ('city', 'state', 'zip','country','phone')