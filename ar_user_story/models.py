from django.db import models
from datetime import datetime
from account.models import AR_organization,Ar_user
import django
###########################################
class AR_FEATURE(models.Model):
    CE_ID  = models.ForeignKey(AR_organization, on_delete=models.CASCADE)
    # ORG_ID   = models.ForeignKey(AR_organization, on_delete=models.CASCADE)
    ORG_ID   = models.IntegerField(default=None,blank=True)
    Feature_key = models.CharField(max_length=50, default="", blank=True)
    Feature_desc = models.TextField(default="", blank=True)
    Children_us_list  = models.CharField(max_length=50, default="", blank=True)
    create_by = models.IntegerField(default="", blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    update_by = models.IntegerField(default="",blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    def __str__(self):
        return str(self.Feature_key)

#
class AR_ITERATIONS(models.Model):
    Iteration_key = models.CharField(max_length=50,blank=True)
    Iteration_desc  = models.TextField(blank=True)
    Assoc_us_list   = models.CharField(max_length=200,blank=True)
    owner   = models.CharField(max_length=200,blank=True)
    TM_ID    = models.ForeignKey(AR_organization, on_delete=models.CASCADE,blank=True)
    create_by = models.IntegerField(blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    update_by = models.IntegerField(blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    def __str__(self):
        return str(self.Iteration_key)
#
class AR_US_TYPE(models.Model):
    type_key  = models.CharField(max_length=50,blank=True)
    type_desc  = models.TextField(blank=True)
    type_short_code   = models.CharField(max_length=50,blank=True)
    create_by = models.IntegerField(blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    update_by = models.IntegerField(blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    def __str__(self):
        return str(self.type_key)
#
class AR_US_STATUS(models.Model):
    status_key  = models.CharField(max_length=50,blank=True)
    status_desc  = models.TextField(blank=True)
    status_shortcode   = models.CharField(max_length=50,blank=True)
    create_by = models.IntegerField(blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    update_by = models.IntegerField(blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    def __str__(self):
        return str(self.status_key)
#
#
class AR_US_POINTS(models.Model):
    point_key  = models.CharField(max_length=50,blank=True)
    point_desc   = models.TextField(blank=True)
    point_short_code   = models.CharField(max_length=50,blank=True)
    create_by = models.IntegerField(blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    update_by = models.IntegerField(blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    def __str__(self):
        return str(self.point_key)
#
# ###########################################
# # Create your models here.
class AR_USER_STORY(models.Model):
    owner = models.CharField(max_length=50,blank=True)
    ar_user = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=80,blank=True)
    user_story_type = models.CharField(max_length=50,blank=True)
    story_tri_part_text = models.TextField(blank=True)
    epic_capability = models.CharField(max_length=80,blank=True)
    feature = models.CharField(max_length=50,blank=True)
    acceptance_criteria = models.TextField(blank=True)
    ac_readability_score = models.IntegerField(blank=True)
    conversation = models.TextField(blank=True)
    convo_readability_score = models.IntegerField(blank=True)
    attachments = models.CharField(max_length=80,blank=True)
    autoscoring_on = models.BooleanField(default=False,blank=True)
    backlog_parent = models.CharField(max_length=100,blank=True)
    user_story_status = models.CharField(max_length=50,blank=True)
    archive_indicator = models.BooleanField(default=False,blank=True)
    readiness_quality_score = models.IntegerField(blank=True)
    story_points = models.IntegerField(blank=True)
    # ft_id = models.BigIntegerField()


    ft_id = models.ForeignKey(AR_FEATURE, on_delete=models.CASCADE, null=True,blank=True)
    itr_id = models.ForeignKey(AR_ITERATIONS, on_delete=models.CASCADE, null=True,blank=True)
    ust_id = models.ForeignKey(AR_US_TYPE, on_delete=models.CASCADE, null=True,blank=True)
    ########################################################################################################
    # bl_id = models.ForeignKey(AR_FEATURE, on_delete=models.CASCADE)
    ########################################################################################################
    usp_id = models.ForeignKey(AR_US_POINTS, on_delete=models.CASCADE, null=True,blank=True)
    uss_id = models.ForeignKey(AR_US_STATUS, on_delete=models.CASCADE, null=True,blank=True)

    # ft_id = models.ForeignKey(AR_FEATURE, on_delete=models.SET_NULL,related_name='value_ar_feature')
    # itr_id = models.ForeignKey(AR_ITERATIONS, on_delete=models.SET_NULL,related_name='value_ar_iterations')
    # ust_id = models.ForeignKey(AR_US_TYPE, on_delete=models.SET_NULL,related_name='value_ar_us_type')
    # ########################################################################################################
    # bl_id = models.ForeignKey(AR_FEATURE, on_delete=models.SET_NULL,related_name='value_bl_id')
    # ########################################################################################################
    # usp_id = models.ForeignKey(AR_US_POINTS, on_delete=models.SET_NULL,related_name='value_usp_id')
    # uss_id = models.ForeignKey(AR_US_STATUS, on_delete=models.SET_NULL,related_name='value_uss_id')
    created_by = models.BigIntegerField(default=None,null=True,blank=True)
    updated_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    created_dt = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    updated_by = models.BigIntegerField(default=None,null=True,blank=True)
    def __str__(self):
        return str(self.owner)
