from django.db import models
import django
from account.models import Ar_user,AR_organization


# Create your models here.
class ArUserProfile(models.Model):
    profile_key = models.CharField(max_length=50,blank=True)
    ORG_ID = models.ForeignKey(AR_organization, on_delete='models.SET_NULL', related_name='userprofile_by_organization')
    create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_userprofile')
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_userprofile')
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.profile_key)


class ArUserProfilePermission(models.Model):
    profile_key = models.ForeignKey(ArUserProfile, on_delete='models.SET_NULL', related_name='userprofilepermission_by_userprofile')
    ORG_ID = models.ForeignKey(AR_organization, on_delete='models.SET_NULL', related_name='userprofilepermission_by_organization')
##################################################################
    activites = models.CharField(max_length=80)
    editor = models.BooleanField(default=False)
    viewer = models.BooleanField(default=False)
##################################################################
    create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_userprofilepermission')
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_userprofilepermission')
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.profile_key)
