from django import forms
from .models import AR_team,AR_product
from account.models import AR_organization,Ar_user
from django.db.models import Subquery
from manage_backlogs.models import AR_BACKLOG
from agileproject.threadlocals import get_current_user


# currentUser = get_current_user()
# currentUserID = currentUser.id
# CHOICES = (('', currentUserID),('Option 2', 'Option 2'),)
# CHOICES_dis = {"":currentUserID,"0":0}
CHOICES = list = [(k, k) for k in range(0,100)]

class ProductForm(forms.ModelForm):
    Product_name          = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Product Name *",}))
    Product_description   = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",}))
    Business_unit          = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",'placeholder':"Business Unit *", }))
    # Product_size           = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control","readonly":"readonly","value":"0"}))
    # Product_score          = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control","readonly":"readonly","value":"0" }))
    US_quality_threshold   = forms.CharField(widget=forms.Select(choices=CHOICES,attrs={"class": "editableBox ssgg","style":"height: 35px!important;"}))


    class Meta:
        model = AR_product
        fields = ['Product_name','Product_description','Team_parent','Business_unit','US_quality_threshold']
        # fields = ['Product_name','Product_description','Team_parent','Business_unit','Product_size','Product_score','US_quality_threshold']

    def __init__(self, user,org_id,*args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        org_info = AR_organization.objects.filter(id=org_id)
        # self.fields['ORG_ID'].queryset = AR_organization.objects.filter(id__in=Subquery(org_info.values("id")))
        self.fields['Team_parent'].queryset = AR_team.objects.filter(ORG_id__in=Subquery(org_info.values("id")))
        # self.fields['Team_parent'] = forms.ModelChoiceField(required=False, empty_label="Please select team",
        #                                                   queryset=AR_team.objects.filter(
        #                                                       ORG_id__in=Subquery(org_info.values("id"))),
        #                                                   widget=forms.Select(attrs={"class": "form-control"}))
        # self.fields['Children_backlog_list'].queryset = AR_BACKLOG.objects.filter(ORG_ID__in=Subquery(org_info.values("id")))
        # self.fields['Team_parent'].queryset = AR_team.objects.filter(ORG_id=org_info)