from django.db import models
from account.models import Ar_user,AR_organization
import django
# Create your models here.

class ArTestcondSet(models.Model):
    member_product_list = models.CharField(max_length=100,null=True,blank=True)
    member_scenario_list = models.CharField(max_length=100,null=True,blank=True)
    testcond_validation_list = models.TextField()
    Use_in = models.TextField()
    ORG_ID = models.ForeignKey(AR_organization,  default="",null=True , on_delete=models.SET_NULL)
    created_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL, related_name='create_by_ArTestcondSet',null=True )
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL, related_name='update_by_ArTestcondSet',null=True )
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.member_product_list)
    class Meta:
        verbose_name_plural = "Ar Test Condition Set"
