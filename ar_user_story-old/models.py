from django.db import models
from datetime import datetime
from account.models import AR_organization,Ar_user
import django
###########################################
class AR_FEATURE(models.Model):
    Feature_key = models.CharField(max_length=50, default=None,blank=True)
    Feature_desc = models.TextField( default=None,blank=True)
    Children_us_list  = models.CharField(max_length=50, default=None,blank=True)
    CE_ID  = models.ForeignKey(AR_organization, on_delete=models.CASCADE)
    # ORG_ID   = models.ForeignKey(AR_organization, on_delete='models.CASCADE')
    ORG_ID   = models.IntegerField(default=None,blank=True)
    create_by = models.IntegerField(default=None,blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    update_by = models.IntegerField(default=None,blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    def __str__(self):
        return str(self.Feature_key)



class AR_ITERATIONS(models.Model):
    Iteration_key = models.CharField(max_length=50)
    Iteration_desc  = models.TextField()
    Assoc_us_list   = models.CharField(max_length=200)
    owner   = models.CharField(max_length=200)
    TM_ID    = models.ForeignKey(AR_organization, on_delete='models.CASCADE')
    create_by = models.IntegerField()
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.IntegerField()
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.Iteration_key)

class AR_US_TYPE(models.Model):
    type_key  = models.CharField(max_length=50)
    type_desc  = models.TextField()
    type_short_code   = models.CharField(max_length=50)
    create_by = models.IntegerField()
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.IntegerField()
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.type_key)

class AR_US_STATUS(models.Model):
    status_key  = models.CharField(max_length=50)
    status_desc  = models.TextField()
    status_shortcode   = models.CharField(max_length=50)
    create_by = models.IntegerField()
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.IntegerField()
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.status_key)


class AR_US_POINTS(models.Model):
    point_key  = models.CharField(max_length=50)
    point_desc   = models.TextField()
    point_short_code   = models.CharField(max_length=50)
    create_by = models.IntegerField()
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.IntegerField()
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.point_key)

###########################################
# Create your models here.
class AR_USER_STORY(models.Model):
    owner = models.CharField(max_length=50)
    ar_user = models.CharField(max_length=50)
    title = models.CharField(max_length=80)
    user_story_type = models.CharField(max_length=50)
    story_tri_part_text = models.TextField()
    epic_capability = models.CharField(max_length=80)
    feature = models.CharField(max_length=50)
    acceptance_criteria = models.TextField()
    ac_readability_score = models.IntegerField()
    conversation = models.TextField()
    convo_readability_score = models.IntegerField()
    attachments = models.CharField(max_length=80)
    autoscoring_on = models.BooleanField(default=False)
    backlog_parent = models.CharField(max_length=100)
    user_story_status = models.CharField(max_length=50)
    archive_indicator = models.BooleanField(default=False)
    readiness_quality_score = models.IntegerField()
    story_points = models.IntegerField()
    # ft_id = models.BigIntegerField()
    ft_id = models.ForeignKey(AR_FEATURE, on_delete='models.SET_NULL',related_name='value_ar_feature')
    itr_id = models.ForeignKey(AR_ITERATIONS, on_delete='models.SET_NULL',related_name='value_ar_iterations')
    ust_id = models.ForeignKey(AR_US_TYPE, on_delete='models.SET_NULL',related_name='value_ar_us_type')
    ########################################################################################################
    bl_id = models.ForeignKey(AR_FEATURE, on_delete='models.SET_NULL',related_name='value_bl_id')
    ########################################################################################################
    usp_id = models.ForeignKey(AR_US_POINTS, on_delete='models.SET_NULL',related_name='value_usp_id')
    uss_id = models.ForeignKey(AR_US_STATUS, on_delete='models.SET_NULL',related_name='value_uss_id')
    created_by = models.BigIntegerField()
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.BigIntegerField()
    def __str__(self):
        return str(self.owner)
