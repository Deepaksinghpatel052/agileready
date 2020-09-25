from django.db import models
import django
from account.models import AR_organization,Ar_user

from autoslug import AutoSlugField



# Create your models here.
class AR_BUSINESS_VALUE(models.Model):
    bus_value_position = models.BigIntegerField(blank=True)
    business_value_slug = AutoSlugField(populate_from='bus_value_txt_code', always_update=True, unique_with='ORG_ID', null=True, blank=True)

    bus_value_txt_code = models.CharField(max_length=50, default="", blank=True)
    bus_value_desc  = models.TextField(default="", blank=True)
    ORG_ID   = models.ForeignKey(AR_organization,default="",null=True , on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.bus_value_txt_code)
    class Meta:
        verbose_name_plural = "Ar Business Value"