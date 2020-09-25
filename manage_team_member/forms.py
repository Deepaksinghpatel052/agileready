from django import forms
from account.models import Ar_user,ArUserProfile
from manage_product.models import AR_product
from django.db.models import Subquery


class ManageTeamMemberForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'readonly':"",'placeholder':"Epic Capability Key *",'name':'user_story_type'}))
    class Meta:
        model = Ar_user
        fields = ['user_name', 'profile_permission']
    def __init__(self,org_info,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_permission'].queryset = ArUserProfile.objects.filter(ORG_ID__in=Subquery(org_info.values("id")))
        self.fields['profile_permission'].widget.attrs={"class": "form-control","style":"float:right; width:100%;"}
        #
        # self.fields['profile_permission'] = forms.ModelChoiceField(required=False, empty_label="Please select team",
        #                                                     queryset=ArUserProfile.objects.filter(ORG_ID__in=Subquery(org_info.values("id"))),
        #                                                     widget=forms.Select(attrs={"class": "form-control","style":"float:right; width:100%;"}))

