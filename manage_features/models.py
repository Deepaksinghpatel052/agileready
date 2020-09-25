from django.db import models
import django
from account.models import AR_organization,Ar_user
from business_value.models import AR_BUSINESS_VALUE
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from user_story_view.models import AR_USER_STORY
from autoslug import AutoSlugField



# Create your models here.
class AR_FEATURE(models.Model):
    Feature_key = models.CharField(max_length=50, default="", blank=True)
    feature_slug = AutoSlugField(populate_from='Feature_key', always_update=True, unique_with='create_dt__month', null=True, blank=True)
    Feature_desc = models.TextField(default="", blank=True)
    CE_ID  = models.ForeignKey(AR_EPIC_CAPABILITY, default="", null=True, on_delete=models.SET_NULL, related_name='epic_from_feature')
    BV_ID  = models.ForeignKey(AR_BUSINESS_VALUE, default="", null=True, on_delete=models.SET_NULL, related_name='business_for_feature')
    ORG_ID   = models.ForeignKey(AR_organization,default="",null=True , on_delete=models.SET_NULL)
    User_story = models.ManyToManyField(AR_USER_STORY, default="",blank=True)
    create_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_feature',null=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_feature',null=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return str(self.Feature_key)
    class Meta:
        verbose_name_plural = "Ar feature"