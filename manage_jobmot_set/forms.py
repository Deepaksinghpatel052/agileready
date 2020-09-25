from django import forms
from .models import ArJobmotSet

class ArJobmotSetForm(forms.ModelForm):
    member_product_list = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Motivation Title"}))
    jobmot_validation_list = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Motivation Description"}))
    Use_in = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Use in Job Stories","readonly":"readonly"}))

    class Meta:
        model = ArJobmotSet
        fields = ['member_product_list', 'jobmot_validation_list', 'Use_in']


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)