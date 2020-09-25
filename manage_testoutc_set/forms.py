from django import forms
from .models import ArTestoutcSet

class ArTestoutcSetForm(forms.ModelForm):
    member_product_list = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Member Product List"}))
    member_scenario_list = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control login-frm-input", "placeholder":"Member Scenario List"}))
    testoutc_validation_list = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Testoutc Validation List"}))
    Use_in = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Use in Test Stories","readonly":"readonly"}))


    class Meta:
        model = ArTestoutcSet
        fields = ['member_product_list', 'member_scenario_list', 'testoutc_validation_list','Use_in']


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)