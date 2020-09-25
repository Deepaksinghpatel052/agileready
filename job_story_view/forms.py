from django import forms
from django.shortcuts import get_object_or_404
from .models import AR_JOB_STORY
from user_story_view.models import AR_US_STATUS,AR_US_TYPE
from user_story_points.models import ArUserStoryPoints
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from django.db.models import Subquery,Q
from account.models import Ar_user,AR_organization
from manage_features.models import AR_FEATURE
from manage_backlogs.models import AR_BACKLOG
from business_value.models import AR_BUSINESS_VALUE



class Ar_Job_Story_Form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'title','placeholder':"Title"}))
    UST_ID = forms.ModelChoiceField(empty_label="Please select user story type or None",queryset=AR_US_TYPE.objects.all(),widget=forms.Select(attrs={"class": "form-control"}))
    story_tri_part_text = forms.CharField(required=False,widget=forms.Textarea(attrs={"class": "form-control login-frm-input", "style": "height: 100px!important;    padding: 11px;", "placeholder": "Description", 'name': 'story_tri_part_text'}))
    acceptance_criteria = forms.CharField(required=False,widget=forms.Textarea(attrs={"class": "form-control login-frm-input", "style": "height: 100px!important;    padding: 11px;","placeholder": "Description", 'name': 'acceptance_criteria'}))
    conversation = forms.CharField(required=False,widget=forms.Textarea(attrs={"class": "form-control login-frm-input", "style": "height: 100px!important;    padding: 11px;","placeholder": "Description", 'name': 'conversation'}))
    readiness_quality_score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'readiness_quality_score',"value":"0","readonly":"readonly"}))
    ac_readability_score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'ac_readability_score',"value":"0","readonly":"readonly"}))
    convo_readability_score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'convo_readability_score',"value":"0","readonly":"readonly"}))
    attachments = forms.FileField(required=False)
    autoscoring_on = forms.BooleanField(required=False, initial=True)
    archive_indicator = forms.BooleanField(required=False)
    job_story_status = forms.ModelChoiceField(empty_label="Please select user story status or None", queryset=AR_US_STATUS.objects.all(),widget=forms.Select(attrs={"class": "form-control"}))
    class Meta:
        model = AR_JOB_STORY
        fields = ['title','owner', 'story_tri_part_text', 'acceptance_criteria','BV_ID', 'ac_readability_score','conversation', 'convo_readability_score', 'attachments','autoscoring_on', 'archive_indicator','readiness_quality_score', 'story_points', 'job_story_status','UST_ID','ar_user','backlog_parent']

    def __init__(self, user_id,org_info, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['story_points'] = forms.ModelChoiceField(required=False, empty_label="Please select user story point or None", queryset=ArUserStoryPoints.objects.filter(ORG_ID=org_info), widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['ar_user'] = forms.ModelChoiceField(empty_label="Please select team member author or None",queryset=Ar_user.objects.filter(~Q(user_name="")).filter(org_id=org_info),widget=forms.Select(attrs={"class": "form-control", 'name': 'ar_user'}))
        self.fields['owner'] = forms.ModelChoiceField(required=False,empty_label="Please select team member owner - Assigned to or None",initial=user_id,queryset=Ar_user.objects.filter(~Q(user_name="")).filter(org_id=org_info), widget=forms.Select(attrs={"class": "form-control",'placeholder':"Owner"}))

        self.fields['backlog_parent'] = forms.ModelChoiceField(empty_label="Please select backlog or None",queryset=AR_BACKLOG.objects.filter(ORG_ID=org_info),widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['BV_ID'] = forms.ModelChoiceField(empty_label="Please select Business Value or None",queryset=AR_BUSINESS_VALUE.objects.filter(ORG_ID=org_info),widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['attachments'].widget.attrs={"class": "form-control",'multiple':True}
