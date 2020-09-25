from django import forms
from .models import ArManageBenefits

class ArManageBenefitsForm(forms.ModelForm):
    Benefits_title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Benefits Title"}))
    Benefits_description = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Description"}))
    Use_in = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Use in User Storyes","readonly":"readonly"}))

    class Meta:
        model = ArManageBenefits
        fields = ['Benefits_title', 'Benefits_description', 'Use_in']


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)