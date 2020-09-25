from django import forms
from .models import ArIterations
from manage_product.models import AR_product,AR_team
from manage_backlogs.models import AR_BACKLOG
from django.db.models import Q,Subquery
from user_story_view.models import AR_USER_STORY
from account.models import Ar_user
import string
import random


class IterationForm(forms.ModelForm):
    IterationName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Iteration Name", }))
    Description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control login-frm-input", "style": "height: 100px!important;","placeholder": "Description", }))
    class Meta:
        model = ArIterations
        fields = ['IterationName', 'owner','Description', 'Product','Backlog','UserStory','Team']
        # fields = ['IterationName', 'owner','Description', 'Product','Backlog','UserStory','Team','IterationScore','IterationSize']
    def __init__(self, org_info,user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Product'] = forms.ModelChoiceField(required=False,empty_label="Please select product or None",queryset=AR_product.objects.filter(ORG_ID__in=Subquery(org_info.values("id"))),widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['Backlog'] = forms.ModelChoiceField(required=False,empty_label="Please select backlog or None",queryset=AR_BACKLOG.objects.none(),widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['owner'] = forms.ModelChoiceField(empty_label="Please select owner or None",initial=user_id,queryset=Ar_user.objects.filter(~Q(user_name="")).filter(org_id__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control",'placeholder':"Owner"}))
        if 'Product' in self.data:
            try:
                Product_id = int(self.data.get('Product'))
                Backlog_id = int(self.data.get('Backlog'))
                self.fields['Backlog'] = forms.ModelChoiceField(required=False, empty_label="Please select backlog or None", queryset=AR_BACKLOG.objects.filter(product_parent=Product_id),widget=forms.Select(attrs={"class": "form-control"}))
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Backlog'] = forms.ModelChoiceField(required=False, empty_label="Please select backlog or None",queryset=AR_BACKLOG.objects.filter(product_parent=self.instance.Product),widget=forms.Select(attrs={"class": "form-control"}))
        self.fields['Team'] = forms.ModelChoiceField(required=False, empty_label="Please select team or None",queryset=AR_team.objects.filter( ORG_id__in=Subquery(org_info.values("id"))),widget=forms.Select(attrs={"class": "form-control"}))
