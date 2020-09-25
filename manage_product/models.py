
from django.db import models
from account.models import Ar_user,AR_organization
from datetime import datetime
import django

from autoslug import AutoSlugField
# Create your models here.



class AR_team(models.Model):
    Team_name = models.CharField(max_length=100)
    team_slug = AutoSlugField(populate_from='Team_name', always_update=True, unique_with='create_dt__month', null=True, blank=True)
    Team_description = models.TextField()
    ORG_id = models.ForeignKey(AR_organization,default="",null=True , on_delete=models.CASCADE)
    Team_member_list = models.ManyToManyField(Ar_user,blank=True, related_name='user_data')
    create_by = models.ForeignKey(Ar_user,on_delete=models.SET_NULL,related_name='create_by_team',null=True ,blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_team',null=True ,blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    class Meta:
        unique_together = ('Team_name', 'ORG_id',)
        verbose_name_plural = "Ar team"
    def __str__(self):
        return str(self.Team_name)


class AR_product(models.Model):
    Product_name = models.CharField(max_length=50)
    product_slug = AutoSlugField(populate_from='Product_name', always_update=True, unique_with='create_dt__month', null=True, blank=True)
    Product_description = models.TextField()
    Team_parent = models.ManyToManyField(AR_team,blank=True, related_name='user_favourite')
    # Children_backlog_list = models.TextField()
    # Children_backlog_list = models.ManyToManyField(AR_team,blank=True, related_name='backlog_favourite')
    Business_unit = models.CharField(max_length=100)
    Product_size = models.IntegerField(default=0)
    Product_score  = models.IntegerField(default=0)
    US_quality_threshold  = models.IntegerField(default=0)
    ORG_ID = models.ForeignKey(AR_organization,default="",null=True ,on_delete=models.SET_NULL)
    create_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_product',null=True ,blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_product',null=True ,blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return self.Product_name
    class Meta:
        verbose_name_plural = "Ar product"



