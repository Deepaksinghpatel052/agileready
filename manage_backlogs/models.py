from django.db import models
import django
from account.models import Ar_user,AR_organization
from manage_product.models import AR_product
from manage_product.models import AR_team
from django.contrib.auth.models import User

from autoslug import AutoSlugField



# Create your models here.
###########################

class AR_BACKLOG_STATUS(models.Model):
    bl_status_key   = models.CharField(max_length=50,blank=True)
    bl_status_desc  = models.TextField(blank=True)
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='create_by_backlogstatus',null=True,blank=True )
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='update_by_backlogstatus',null=True,blank=True )
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.bl_status_key)
    class Meta:
        verbose_name_plural = "Ar backlog status"
###########################

class AR_BACKLOG(models.Model):
    title = models.CharField(max_length=100)
    backlog_description = models.TextField()

    backlog_slug = AutoSlugField(populate_from='title', always_update=True, unique_with='created_dt__month', null=True, blank=True)

    # product_parent = models.CharField(max_length=50)
    # children_us_list = models.TextField(blank=True)
    owner = models.ForeignKey(Ar_user,  default="",null=True , on_delete=models.SET_NULL)
    backlog_score = models.IntegerField()
    Backlog_size = models.IntegerField()
    # team_list = models.ForeignKey(AR_team,  default="",null=True , on_delete='models.SET_NULL')


    team_list = models.ManyToManyField(AR_team,blank=True, related_name='backlog_team')
    product_parent = models.ForeignKey(AR_product,  default="",null=True , on_delete=models.SET_NULL, related_name='backlog_by_product')


    BL_STATUS = models.ForeignKey(AR_BACKLOG_STATUS,  default="",null=True , on_delete=models.SET_NULL)
    ORG_ID = models.ForeignKey(AR_organization,  default="",null=True , on_delete=models.SET_NULL)
    created_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_backlog',null=True )
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_backlog',null=True )
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "Ar backlog"

