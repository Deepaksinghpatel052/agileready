from django import forms
from .models import AR_SCENARIO
from manage_product.models import AR_product
from account.models import AR_organization,Ar_user
from django.db.models import Subquery
from manage_backlogs.models import AR_BACKLOG
from agileproject.threadlocals import get_current_user


CHOICES = list = [(k, k) for k in range(0,100)]


class ScenarioForm(forms.ModelForm):
    scenario_name          = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Scenario Name *",}))
    scenario_desc   = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",}))

    class Meta:
        model = AR_SCENARIO
        fields = ['scenario_name','scenario_desc','product_id']

    def __init__(self, user,org_id,*args, **kwargs):
        # self.user = user
        super().__init__(*args, **kwargs)
        org_info = AR_organization.objects.filter(id=org_id)
        self.fields['product_id'] = forms.ModelChoiceField(required=False, empty_label="Please select product or None",queryset=AR_product.objects.filter(ORG_ID__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control"}))
