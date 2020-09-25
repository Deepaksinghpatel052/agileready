from django import forms
from .models import ArRole
from django.db.models import Subquery


class ArRoleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Role Title *",'name':'role_title'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",'name':'role_desc'}))
    use = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","readonly":"readonly","style":"height: 100px!important;   padding: 11px;","placeholder":"Use in User Storyes"}))
    class Meta:
        model = ArRole
        fields = ['title', 'desc','use']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)