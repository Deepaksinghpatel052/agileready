from django.db import models
import django
from account.models import AR_organization,Ar_user

# Create your models here.
###########################
class ArRole(models.Model):
    role_id   = models.CharField(max_length=50,blank=True)
    title  = models.CharField(max_length=50,blank=True)
    desc = models.TextField(blank=True)
    use = models.TextField(blank=True, default="")
    ORG_ID = models.ForeignKey(AR_organization, default="", null=True, on_delete=models.SET_NULL)
    create_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_role',null=True ,blank=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_role',null=True ,blank=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return str(self.role_id)
    class Meta:
        verbose_name_plural = "Ar role"
###########################