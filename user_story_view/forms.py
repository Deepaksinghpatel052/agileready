from django import forms
from django.shortcuts import get_object_or_404
from .models import AR_USER_STORY,AR_US_STATUS,AR_US_TYPE
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from django.db.models import Subquery,Q
from account.models import Ar_user,AR_organization
from manage_features.models import AR_FEATURE
from manage_backlogs.models import AR_BACKLOG
from manage_iterations.models import AR_ITERATIONS


class Ar_User_Story_Form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'title'}))
    owner = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'owner'}))
    UST_ID = forms.ModelChoiceField(queryset=AR_US_TYPE.objects.all(),widget=forms.Select(attrs={"class": "form-control"}))
    story_tri_part_text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control login-frm-input", "style": "height: 100px!important;    padding: 11px;", "placeholder": "Description", 'name': 'story_tri_part_text'}))
    acceptance_criteria = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control login-frm-input", "style": "height: 100px!important;    padding: 11px;","placeholder": "Description", 'name': 'acceptance_criteria'}))
    conversation = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control login-frm-input", "style": "height: 100px!important;    padding: 11px;","placeholder": "Description", 'name': 'conversation'}))
    readiness_quality_score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'readiness_quality_score'}))
    ac_readability_score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'ac_readability_score'}))
    convo_readability_score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'convo_readability_score'}))
    attachments = forms.FileField()
    autoscoring_on = forms.BooleanField(required=False)
    archive_indicator = forms.BooleanField(required=False)
    user_story_status = forms.ModelChoiceField(queryset=AR_US_STATUS.objects.all(),widget=forms.Select(attrs={"class": "form-control"}))
    story_points = forms.ModelChoiceField(queryset=AR_EPIC_CAPABILITY.objects.all(),widget=forms.Select(attrs={"class": "form-control"}))
    class Meta:
        model = AR_USER_STORY
        fields = ['title','owner', 'story_tri_part_text', 'acceptance_criteria', 'ac_readability_score','conversation', 'convo_readability_score', 'attachments','autoscoring_on', 'archive_indicator','readiness_quality_score', 'story_points', 'user_story_status','UST_ID','ar_user','backlog_parent']

    def __init__(self, org_info, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # filter(ORG_ID=org_info)
        org_instance =get_object_or_404(AR_organization, pk=org_info)
        # self.fields['backlog_parent'] = forms.ModelChoiceField(queryset=AR_BACKLOG.objects.filter(ORG_ID__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['ar_user'] = forms.ModelChoiceField(queryset=Ar_user.objects.filter(~Q(user_name="")).filter(org_id=org_info),widget=forms.Select(attrs={"class": "form-control", 'name': 'ar_user'}))
        self.fields['backlog_parent'] = forms.ModelChoiceField(queryset=AR_BACKLOG.objects.filter(ORG_ID=org_info),widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['attachments'].widget.attrs = {"class": "form-control"}
