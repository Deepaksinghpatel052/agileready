from django.db import models
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from account.models import Ar_user,AR_organization
from manage_iterations.models import AR_ITERATIONS
from manage_backlogs.models import AR_BACKLOG
import django
import os
# Create your models here.



class AR_US_STATUS(models.Model):
    status_key  = models.CharField(max_length=50,blank=True,unique=True)
    status_desc  = models.TextField(blank=True)
    status_shortcode   = models.CharField(max_length=50,blank=True,unique=True)
    create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_us_status',default="")
    create_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True,null=True)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',default="",related_name='update_by_us_status')
    update_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True,null=True)
    def __str__(self):
        return str(self.status_key)


class AR_US_TYPE(models.Model):
    type_key  = models.CharField(max_length=50,blank=True,unique=True)
    type_desc  = models.TextField(blank=True)
    type_short_code   = models.CharField(max_length=50,blank=True,unique=True)
    create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',default="",related_name='create_by_us_type',blank=True,null=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',default="",related_name='update_by_us_type',blank=True,null=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.type_key)


class AR_USER_STORY(models.Model):
    owner = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=80,blank=True)
    story_tri_part_text = models.TextField(blank=True)
    acceptance_criteria = models.TextField(blank=True)
    ac_readability_score = models.IntegerField(blank=True)
    conversation = models.TextField(blank=True)
    backlog_parent = models.ForeignKey(AR_BACKLOG, on_delete=models.SET_DEFAULT,default=None)
    convo_readability_score = models.IntegerField(blank=True)
    attachments = models.FileField(upload_to='attachments/')
    autoscoring_on = models.BooleanField(default=False,blank=True)
    archive_indicator = models.BooleanField(default=False,blank=True)
    readiness_quality_score = models.IntegerField(blank=True)
    story_points = models.ForeignKey(AR_EPIC_CAPABILITY,related_name='story_points', on_delete=models.CASCADE)
    user_story_status = models.ForeignKey(AR_US_STATUS, on_delete=models.CASCADE)
    ORG_id = models.ForeignKey(AR_organization, on_delete=models.SET_DEFAULT,default=None)
    UST_ID = models.ForeignKey(AR_US_TYPE, on_delete=models.SET_DEFAULT,default=None)
    ar_user = models.ForeignKey(Ar_user, on_delete=models.SET_DEFAULT,default=None)
    created_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_user_story')
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_user_story')
    def __str__(self):
        return str(self.title)

    def filename(self):
        return os.path.basename(self.attachments.name)
