from django.db import models
from account.models import Ar_user,AR_organization
import django
# Create your models here.

class ArManageGoals(models.Model):
    Goal_id = models.CharField(max_length=50,null=True,blank=True)
    Goal_title = models.CharField(max_length=50,null=True,blank=True)
    Gole_description = models.TextField()
    Use_in = models.TextField()
    ORG_ID = models.ForeignKey(AR_organization,  default="",null=True , on_delete=models.SET_NULL)
    created_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL, related_name='create_by_ManageGoals',null=True)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL, related_name='update_by_ManageGoals',null=True)
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return str(self.Goal_title)
    class Meta:
        verbose_name_plural = "Ar manage goals"
