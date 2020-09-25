from django import forms
from account.models import ArUserProfile

class ArUserProfileForm(forms.ModelForm):
    profile_key = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'style':"width:100%;", 'placeholder':"Profile Key",'name':'user_story_type'}))
    class Meta:
        model = ArUserProfile
        fields = ['profile_key']

