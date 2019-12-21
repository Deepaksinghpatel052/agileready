from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import django

# Create your models here.

class Ar_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, default=None,blank=True)
    address = models.CharField(max_length=255, default="", blank=True)
    city = models.CharField(max_length=255, default="", blank=True)
    state = models.CharField(max_length=255, default="", blank=True)
    zip = models.IntegerField(default="", blank=True)
    country = models.CharField(max_length=50, default="", blank=True)
    phone = models.BigIntegerField(default="", blank=True)
    backup_email = models.EmailField(max_length=50, default="", blank=True)
    user_type = models.CharField(max_length=50, default="Root")
    login_status = models.BooleanField(default=False)
    activate_status = models.BooleanField(default=False)
    org_id = models.CharField(max_length=50,default=0)
    verification_status = models.BooleanField(default=False)
    created_by = models.IntegerField(default=0)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.IntegerField(default=0)
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.user_name)


class AR_organization_status(models.Model):
    status_key = models.CharField(max_length=50)
    status_desc = models.TextField(blank=True)
    created_by = models.ForeignKey(User, related_name='person2personsstatuStatus', on_delete=models.SET_NULL,null=True )
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(User, related_name='friendsStatus', on_delete=models.SET_NULL,null=True )
    update_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.status_key)


class AR_organization(models.Model):
    org_id = models.CharField(max_length=50, unique=True)
    organization_name = models.CharField(max_length=100)
    organization_url = models.URLField(max_length=50, default="", blank=True)
    address = models.TextField(blank=True)
    subscription_level = models.CharField(blank=True, max_length=50)
    organization_status = models.ForeignKey(AR_organization_status, on_delete=models.SET_NULL, default="",blank=True,null=True )
    created_by = models.ForeignKey(User, related_name='person2personsorganization', on_delete=models.SET_NULL,null=True )
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(User, related_name='friendsorganization', on_delete=models.SET_NULL,null=True )
    update_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.organization_name)
