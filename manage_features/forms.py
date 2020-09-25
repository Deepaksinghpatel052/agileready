from django import forms
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from business_value.models import AR_BUSINESS_VALUE
from .models import AR_FEATURE
from manage_product.models import AR_product
from user_story_view.models import AR_USER_STORY
from django.db.models import Subquery


class Ar_Featurre_Form(forms.ModelForm):
    Feature_key = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Feature Key *",'name':'user_story_type'}))
    Feature_desc = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",'name':'story_tri_part_text'}))
    class Meta:
        model = AR_FEATURE
        # fields = ['Feature_key', 'Feature_desc', 'CE_ID','User_story']
        fields = ['Feature_key', 'Feature_desc', 'CE_ID','BV_ID','User_story']
        # fields = ['Cepic_key', 'Cepic_desc']
    def __init__(self,org_info,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['CE_ID'] = forms.ModelChoiceField(required=False, empty_label="Please select capability or None",queryset=AR_EPIC_CAPABILITY.objects.filter(ORG_ID__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['BV_ID'] = forms.ModelChoiceField(required=False, empty_label="Please select business value or None",queryset=AR_BUSINESS_VALUE.objects.filter(ORG_ID__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['User_story'].queryset = AR_USER_STORY.objects.filter(ORG_id__in=Subquery(org_info.values("id")))
        #
        # self.fields['User_story'] = forms.ModelChoiceField(required=False, empty_label="Please select user story",
        #                                              queryset=AR_USER_STORY.objects.filter(
        #                                                  ORG_id__in=Subquery(org_info.values("id"))),
        #                                              widget=forms.Select(attrs={"class": "form-control"}))

        # self.fields['CE_ID'].queryset = AR_EPIC_CAPABILITY.objects.filter(ORG_ID__in=Subquery(org_info.values("id")))

        # self.fields['CE_ID'] = forms.ModelMultipleChoiceField(queryset=AR_EPIC_CAPABILITY.objects.filter(ORG_ID__in=Subquery(org_info.values('id'))), widget=forms.SelectMultiple(attrs={"class": "form-control"}))
