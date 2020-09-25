from django import forms
from .models import AR_BUSINESS_VALUE
from django.db.models import Subquery


class ArBusinessValueForm(forms.ModelForm):
    bus_value_position = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control",'placeholder':"Business Value Position *",'name':'business_position'}))
    bus_value_txt_code = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Business Value Text Code *",'name':'business_text_code'}))
    bus_value_desc = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","placeholder":"Business Value Description","style":"height: 100px!important;   padding: 11px;"}))
    class Meta:
        model = AR_BUSINESS_VALUE
        fields = ['bus_value_position', 'bus_value_txt_code','bus_value_desc']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)