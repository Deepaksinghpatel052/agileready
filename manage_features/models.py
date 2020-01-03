from django.db import models
import django
from account.models import AR_organization,Ar_user
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from user_story_view.models import AR_USER_STORY



# Create your models here.
class AR_FEATURE(models.Model):
    Feature_key = models.CharField(max_length=50, default="", blank=True)
    Feature_desc = models.TextField(default="", blank=True)
    CE_ID  = models.ForeignKey(AR_EPIC_CAPABILITY, on_delete='models.SET_NULL')
    ORG_ID   = models.ForeignKey(AR_organization, on_delete='models.SET_NULL')
    User_story = models.ForeignKey(AR_USER_STORY,on_delete='models.SET_NULL', default="",blank=True)
    create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_feature')
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_feature')
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.Feature_key)