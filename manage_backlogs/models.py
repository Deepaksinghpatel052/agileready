from django.db import models
import django
from account.models import Ar_user,AR_organization
from manage_product.models import AR_product
from manage_product.models import AR_team



# Create your models here.
###########################
class AR_BACKLOG_STATUS(models.Model):
    bl_status_key   = models.CharField(max_length=50,blank=True)
    bl_status_desc  = models.TextField(blank=True)
    create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_backlogstatus')
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_backlogstatus')
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.bl_status_key)
###########################

class AR_BACKLOG(models.Model):
    title = models.CharField(max_length=100)
    # product_parent = models.CharField(max_length=50)
    children_us_list = models.CharField(max_length=50)
    owner = models.CharField(max_length=100)
    auto_score_flag = models.BooleanField(default=False)
    backlog_score = models.IntegerField()
    Backlog_size = models.IntegerField()
    bl_scoring_history = models.TextField(default="",null=True)
    team_list = models.ForeignKey(AR_team, on_delete='models.SET_NULL')
    product_parent = models.ForeignKey(AR_product, on_delete='models.SET_NULL')
    BL_STATUS = models.ForeignKey(AR_BACKLOG_STATUS, on_delete='models.SET_NULL')
    ORG_ID = models.ForeignKey(AR_organization, on_delete='models.SET_NULL')
    created_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_backlog')
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_backlog')
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.title)

