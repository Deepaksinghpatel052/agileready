from django.db import models
from account.models import Ar_user,AR_organization
from datetime import datetime
import django
# Create your models here.



class AR_team(models.Model):
    Team_name = models.CharField(max_length=100)
    Team_description = models.TextField()
    ORG_id = models.ForeignKey(AR_organization, on_delete='models.CASCADE')
    Team_member_list = models.ManyToManyField(Ar_user,blank=True, related_name='user_data')
    create_by = models.ForeignKey(Ar_user,on_delete='models.SET_NULL',related_name='create_by_team')
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_team')
    update_dt = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        unique_together = ('Team_name', 'ORG_id',)
    def __str__(self):
        return str(self.Team_name)

class AR_product(models.Model):
    Procduct_name = models.CharField(max_length=50)
    Procduct_description = models.TextField()
    Team_parent = models.ManyToManyField(AR_team,blank=True, related_name='user_favourite')
    Children_backlog_list = models.ManyToManyField(AR_team,blank=True, related_name='backlog_favourite')
    Business_unit = models.CharField(max_length=100)
    Product_size = models.IntegerField(default=0)
    Product_score  = models.IntegerField(default=0)
    US_quality_threshold  = models.IntegerField(default=0)
    ORG_ID = models.ForeignKey(AR_organization,on_delete='models.SET_NULL')
    create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_product')
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_product')
    update_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.Procduct_name



