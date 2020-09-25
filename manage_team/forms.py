from django import forms
from manage_product.models import AR_team
from account.models import Ar_user,AR_organization
from django.db.models import Q,Subquery


class ManageTeamForm(forms.ModelForm):
    Team_name  = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Team Name *",}))
    Team_description  = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px; padding: 11px;","placeholder":"Description",}))
    class Meta:
        model = AR_team
        fields = ['Team_name', 'Team_description', 'Team_member_list',]

    def __init__(self, user, org_id,user_objects, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        org_info = AR_organization.objects.filter(id=org_id)
        # Team_info = AR_team.objects.filter(ORG_id=org_info)
        # .filter(~Q(id__in=user_objects))
        self.fields['Team_member_list'].queryset = Ar_user.objects.filter(org_id=org_id).filter(~Q(user_name=''))
        self.fields['Team_member_list'].widget.attrs = {"class":"team_member_class"}
        #
        # self.fields['Team_member_list'] = forms.ModelChoiceField(required=False, empty_label="Please select team member",
        #                                                     queryset=Ar_user.objects.filter(org_id=org_id).filter(~Q(id__in=user_objects)).filter(~Q(user_name='')),
        #                                                     widget=forms.Select(attrs={"class": "team_member_class"}))
