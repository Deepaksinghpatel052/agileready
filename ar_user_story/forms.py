from django import forms
from .models import AR_USER_STORY,AR_FEATURE,AR_ITERATIONS,AR_US_POINTS,AR_US_STATUS,AR_US_TYPE
from account.models import AR_organization,Ar_user
from django.db.models import Subquery

#
CHOICES = list = [(k, k) for k in range(0,100)]
#########################################################################
org_info = AR_organization.objects.filter(organization_name="digimonk1")
############################################################################

class Ar_User_Story_Form(forms.ModelForm):
    # owner = forms.CharField(max_length=100,
    #                                  widget=forms.TextInput
    #                                  (attrs={'name': 'city',
    #                                          'class': 'form-control form-control-lg', 'placeholder': 'Your City'}))


    owner = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'name':'owner'}))
    ar_user = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'name':'ar_user'}))
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'name':'title'}))
    user_story_type = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'name':'user_story_type'}))
    story_tri_part_text = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",'name':'story_tri_part_text'}))
    epic_capability = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'name':'epic_capability'}))
    acceptance_criteria = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",'name':'acceptance_criteria'}))
    conversation = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control login-frm-input","style":"height: 100px!important;    padding: 11px;","placeholder":"Description",'name':'conversation'}))
    backlog_parent = forms.CharField(widget=forms.Select(choices=CHOICES,attrs={"class": "form-control",'name':'backlog_parent'}))
    readiness_quality_score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name':'readiness_quality_score'}))
    ac_readability_score  = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name':'ac_readability_score'}))
    convo_readability_score  = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name':'convo_readability_score'}))
    attachments = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'name':'attachments'}))
    feature = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'name':'feature'}))
    # user_story_status = forms.ChoiceField(widget=forms.TextInput(attrs={"class":"form-control",}))
    # story_points = forms.ChoiceField(widget=forms.NumberInput(attrs={"class": "form-control", }))
    #
    user_story_status = forms.CharField(widget=forms.Select(choices=CHOICES,attrs={"class": "form-control",'name':'user_story_status'}))
    story_points = forms.CharField(widget=forms.Select(choices=CHOICES,attrs={"class": "form-control",'name':'story_points'}))
    # autoscoring_on = forms.BooleanField(widget=forms.BooleanField(attrs={"class":"form-control",}))
    autoscoring_on = forms.BooleanField()
    archive_indicator = forms.BooleanField()
    class Meta:
        model = AR_USER_STORY
        fields = ['owner', 'title', 'user_story_type', 'story_tri_part_text', 'epic_capability', 'feature',
                  'acceptance_criteria', 'conversation',  'autoscoring_on', 'backlog_parent',
                  'user_story_status', 'archive_indicator',
                  'readiness_quality_score', 'story_points','ar_user','ac_readability_score',
                  'convo_readability_score','attachments','ft_id','itr_id','ust_id','uss_id','usp_id']


    # def __init__(self, user,*args, **kwargs):
    def __init__(self,*args, **kwargs):
        # self.user = user
        super().__init__(*args, **kwargs)
        # user_idfo = AR_organization.objects.filter(created_by=user.id)
        # self.fields['ft_id'].queryset = AR_FEATURE.objects.filter(ORG_id__in=Subquery(org_info.values("id")))
        self.fields['ft_id'].queryset = AR_FEATURE.objects.all()
        # self.fields['ft_id'].queryset = AR_FEATURE.objects.filter(ORG_id__in=Subquery(org_info.values("id")))
        self.fields['itr_id'].queryset = AR_ITERATIONS.objects.all()
        self.fields['ust_id'].queryset = AR_US_TYPE.objects.all()
        self.fields['uss_id'].queryset = AR_US_STATUS.objects.all()
        self.fields['usp_id'].queryset = AR_US_POINTS.objects.all()
        # self.fields['Team_parent'].queryset = AR_team.objects.filter(ORG_id=org_info)