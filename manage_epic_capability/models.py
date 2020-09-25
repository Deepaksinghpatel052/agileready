from django.db import models
import django
from account.models import AR_organization,Ar_user
from manage_product.models import AR_product
from autoslug import AutoSlugField


# Create your models here.
class AR_EPIC_CAPABILITY(models.Model):
    Cepic_key   = models.CharField(max_length=50)
    epic_capability_slug = AutoSlugField(populate_from='Cepic_key', always_update=True, unique_with='create_dt__month', null=True, blank=True)
    Cepic_desc    = models.TextField()
    PROJECT_ID  = models.ManyToManyField(AR_product, default="",blank=True, related_name='epic_capability_product')
    ORG_ID   = models.ForeignKey(AR_organization,default="",null=True , on_delete=models.SET_NULL)
    created_by  = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_epic',null=True)
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='update_by_epic',null=True)
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return str(self.Cepic_key)
    class Meta:
        verbose_name_plural = "Ar epic capability"
