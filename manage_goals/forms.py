from django import forms
from .models import ArManageGoals

class ArManageGoalsForm(forms.ModelForm):
    Goal_title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Goal title"}))
    Gole_description = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Description"}))
    Use_in = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Use in User Storyes","readonly":"readonly"}))

    class Meta:
        model = ArManageGoals
        fields = ['Goal_title', 'Gole_description', 'Use_in']


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)