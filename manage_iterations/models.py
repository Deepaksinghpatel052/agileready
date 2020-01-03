from django.db import models
from account.models import Ar_user,AR_organization
from manage_product.models import AR_team
import django
# Create your models here.


class AR_ITERATIONS(models.Model):
    Iteration_key = models.CharField(max_length=50,blank=True)
    Iteration_desc  = models.TextField(blank=True)
    Assoc_us_list   = models.CharField(max_length=200,blank=True)
    owner   = models.CharField(max_length=200,blank=True)
    TM_ID    = models.ForeignKey(AR_team, on_delete=models.CASCADE,blank=True)
    ORG_ID    = models.ForeignKey(AR_organization, on_delete=models.CASCADE,blank=True ,default=None)
    create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_iterations')
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_iterations')
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.Iteration_key)