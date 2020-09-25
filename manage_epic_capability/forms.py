from django import forms
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_product.models import AR_product
from django.db.models import Subquery


class Ar_Epic_Capability_Form(forms.ModelForm):
    Cepic_key = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Epic Capability Key *",'name':'user_story_type'}))
    Cepic_desc = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",'name':'story_tri_part_text'}))
    # Children_feature_list = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'name':'user_story_type'}))
    class Meta:
        model = AR_EPIC_CAPABILITY
        fields = ['Cepic_key', 'Cepic_desc','PROJECT_ID']
    def __init__(self,org_info,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['PROJECT_ID'].queryset = AR_product.objects.filter(ORG_ID__in=Subquery(org_info.values("id")))
        #
        # self.fields['PROJECT_ID'] = forms.ModelChoiceField(required=False, empty_label="Please select product id",
        #                                              queryset=AR_product.objects.filter(
        #                                                  ORG_ID__in=Subquery(org_info.values("id"))),
        #                                              widget=forms.Select(attrs={"class": "form-control"}))

