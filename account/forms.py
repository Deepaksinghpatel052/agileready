from django import forms
from django.contrib.auth.models import User
from .models import Ar_user,csvFilesUplodaded

class UserAuth(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')

class Ar_user(forms.ModelForm):
    class Meta:
        model = Ar_user
        fields = ('city', 'state', 'zip','country','phone')

class csvFilesUplodadedForm(forms.ModelForm):
    attachments = forms.FileField()
    class Meta:
        model = csvFilesUplodaded
        fields = ['attachments']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachments'].widget.attrs = {"class": "form-control","style":"width: 75%;","aria-label":"Recipient's username","aria-describedby":"button-addon2"}


