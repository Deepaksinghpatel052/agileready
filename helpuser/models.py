from django.db import models
from django.contrib.auth.models import User
import django




# Create your models here.
###########################
class Cms_manage(models.Model):
    keyword = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=50,blank=True)
    help_description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='created_by_helpuser',null=True )
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='updated_by_helpuser',null=True )
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "View move content manage"
###########################