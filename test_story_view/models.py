from django.db import models
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from account.models import Ar_user,AR_organization
from user_story_points.models import ArUserStoryPoints
from manage_product.models import AR_product
from ar_scenario.models import AR_SCENARIO


from business_value.models import AR_BUSINESS_VALUE
from user_story_view.models import AR_US_STATUS,AR_US_TYPE,AR_USER_STORY
from django.contrib.auth.models import User
import django
import os
# Create your models here.


class AR_TEST_STORY(models.Model):
    title = models.CharField(max_length=80,blank=True)
    story_tri_part_text = models.TextField(blank=True)
    acceptance_criteria = models.TextField(blank=True)
    ac_readability_score = models.BigIntegerField(blank=True)
    conversation = models.TextField(blank=True)

    product_parent = models.ForeignKey(AR_product,default="",null=True , on_delete=models.SET_DEFAULT, related_name='test_story_by_product')
    scenario_parent = models.ForeignKey(AR_SCENARIO,default="",null=True , on_delete=models.SET_DEFAULT, related_name='test_story_by_scenario')
    BV_ID = models.ForeignKey(AR_BUSINESS_VALUE,default="",null=True , on_delete=models.SET_DEFAULT, related_name='test_story_by_business_value')

    convo_readability_score = models.BigIntegerField(blank=True)
    autoscoring_on = models.BooleanField(default=False,blank=True)
    archive_indicator = models.BooleanField(default=False,blank=True)
    readiness_quality_score = models.BigIntegerField(blank=True)
    story_points = models.ForeignKey(ArUserStoryPoints,default="",null=True ,related_name='test_story_points', on_delete=models.CASCADE)
    test_story_status = models.ForeignKey(AR_US_STATUS,default="",blank=True,null=True , on_delete=models.CASCADE)
    ORG_id = models.ForeignKey(AR_organization,default="",null=True , on_delete=models.SET_DEFAULT)
    UST_ID = models.ForeignKey(AR_US_TYPE,default="",null=True,blank=True , on_delete=models.SET_DEFAULT)
    ar_user = models.ForeignKey(Ar_user,default="",null=True , on_delete=models.SET_NULL,related_name='test_story_ar_user')
    owner = models.ForeignKey(Ar_user,  default="",null=True , on_delete=models.SET_NULL)
    created_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_test_story',null=True ,blank=True)
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_test_story',null=True ,blank=True)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "Ar bdd tdd story"
    def filename(self):
        return os.path.basename(self.attachments.name)




class test_story_file_attachment(models.Model):
    name  = models.TextField(blank=True)
    attachment = models.FileField(upload_to='attachments/test_story/',default="None", blank = True,null=True)
    test_story = models.ForeignKey(AR_TEST_STORY,default="",null=True , on_delete=models.SET_DEFAULT, related_name='test_story_file_attachment')

    class Meta:
        verbose_name_plural = "Ar test story attachment"
    def __str__(self):
        return str(self.name)
