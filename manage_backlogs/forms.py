from django import forms
from django.db.models import Q,Subquery
from manage_backlogs.models import AR_BACKLOG,AR_BACKLOG_STATUS
from manage_product.models import AR_product,AR_team
from account.models import Ar_user

CHOICES = list = [(1, "Default 1"),(2, "Default 2"),(3, "Default 3"),(4, "Default 4")]

class Ar_Backlog_Form(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",'placeholder':"Title *", 'name': 'title'}))
    backlog_description   = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",}))

    # owner = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",'placeholder':"Owner Name *", 'name': 'owner'}))
    # product_parent = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'product_parent'}))
    BL_STATUS = forms.ModelChoiceField(required=False,empty_label="Please select backlog status or None",queryset=AR_BACKLOG_STATUS.objects.all(), widget=forms.Select(attrs={'placeholder':"Status *","class": "form-control"}))
    bl_scoring_history = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;  padding: 11px;","placeholder":"Description",'name':'story_tri_part_text'}))
    class Meta:
        model = AR_BACKLOG
        fields = ['title',  'owner','BL_STATUS', 'team_list', 'product_parent','backlog_description']
    def __init__(self,org_info,user_id,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'] = forms.ModelChoiceField(empty_label="Please select owner or None",initial=user_id,queryset=Ar_user.objects.filter(~Q(user_name="")).filter(org_id__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control",'placeholder':"Owner"}))
        # self.fields['team_list'] = forms.ModelChoiceField(required=False,empty_label="Please select team or None",queryset=AR_team.objects.filter(ORG_id__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['product_parent'] = forms.ModelChoiceField(empty_label="Please select product or None",queryset=AR_product.objects.filter(ORG_ID__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control",'placeholder':"Product Parent"}))

        self.fields['team_list'].queryset = AR_team.objects.filter(ORG_id__in=Subquery(org_info.values("id")))
        # self.fields['team_list'].widget.attrs = {"class":"team_member_class"}



