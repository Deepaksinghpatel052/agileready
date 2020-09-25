from django.db import models
import django
from datetime import datetime
from account.models import AR_organization,Ar_user
from manage_product.models import AR_product
from autoslug import AutoSlugField



# Create your models here.
class AR_SCENARIO(models.Model):
    scenario_name = models.CharField(max_length=100, default="", blank=True)

    scenario_slug = AutoSlugField(populate_from='scenario_name', always_update=True, unique_with='created_dt__month', null=True, blank=True)

    scenario_desc = models.TextField(default="", blank=True)
    # product_parent  = models.CharField(max_length=50, default="", blank=True)
    # children_us_list   = models.CharField(max_length=50, default="", blank=True)
    # scenario_size = models.BigIntegerField(blank=True)
    # scenario_score = models.BigIntegerField(blank=True)
    product_id  = models.ForeignKey(AR_product,default="",null=True ,related_name='product_by_scenario', on_delete=models.SET_NULL)
    created_by   = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_scenario',null=True ,blank=True)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_scenario',null=True ,blank=True)
    updated_dt  = models.DateTimeField(default=django.utils.timezone.now)
    ORG_ID   = models.ForeignKey(AR_organization,default="",null=True , on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.scenario_name)
    class Meta:
        verbose_name_plural = "Ar Scenario"