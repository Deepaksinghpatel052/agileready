from django import forms
from django.db.models import Subquery
from .models import ArUserStoryPoints
from manage_product.models import AR_product,AR_team
from account.models import Ar_user

# CHOICES = list = [(1, "Default 1"),(2, "Default 2"),(3, "Default 3"),(4, "Default 4")]

class ArStoryPointForm(forms.ModelForm):

    Point_Key = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",'placeholder':"Point Key *", 'name': 'Point_Key'}))
    Point_Description = forms.CharField(required=False,widget=forms.Textarea(attrs={"class": "form-control",'placeholder':"Point Description ", 'name': 'Point_Description'}))

    Point_score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control",'placeholder':"Point Score *", 'name': 'Point_score'}))
    class Meta:
        model = ArUserStoryPoints
        fields = ['Point_Key',  'Point_Description','Point_score']
    def __init__(self,org_info,*args, **kwargs):
        super().__init__(*args, **kwargs)
    #     self.fields['team_list'] = forms.ModelChoiceField(required=False,empty_label="Please select team",queryset=AR_team.objects.filter(ORG_id__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control"}))
    #     self.fields['product_parent'] = forms.ModelChoiceField(required=False,empty_label="Please select product",queryset=AR_product.objects.filter(ORG_ID__in=Subquery(org_info.values("id"))), widget=forms.Select(attrs={"class": "form-control"}))




