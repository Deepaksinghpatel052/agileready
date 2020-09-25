from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import django
from agileproject import settings
# from manage_user_profile.models import ArUserProfile

# Create your models here.




class AR_organization_status(models.Model):
    status_key = models.CharField(max_length=50)
    status_desc = models.TextField(blank=True)
    created_by = models.ForeignKey(User, related_name='person2personsstatuStatus', on_delete=models.SET_NULL,null=True )
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(User, related_name='friendsStatus', on_delete=models.SET_NULL,null=True )
    update_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.status_key)
    class Meta:
        verbose_name_plural = "Ar organization status"


class AR_organization(models.Model):
    org_id = models.CharField(max_length=50, unique=True)
    organization_name = models.CharField(max_length=100)
    organization_url = models.URLField(max_length=50, default="", blank=True)
    address = models.TextField(blank=True)
    subscription_level = models.CharField(blank=True, max_length=50)
    organization_status = models.ForeignKey(AR_organization_status, on_delete=models.SET_NULL, default="",null=True ,blank=True)
    Activate_status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='person2personsorganization', on_delete=models.SET_NULL,null=True )
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(User, related_name='friendsorganization', on_delete=models.SET_NULL,null=True )
    update_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.organization_name)
    class Meta:
        verbose_name_plural = "Ar organization"

###############################################################
class ArUserProfile(models.Model):
    profile_key = models.CharField(max_length=50,blank=True)
    ORG_ID = models.ForeignKey(AR_organization, on_delete=models.SET_NULL,  default="",null=True ,  related_name='userprofile_by_organization')
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='create_by_userprofile',null=True )
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='update_by_userprofile',null=True )
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.profile_key)
    class Meta:
        verbose_name_plural = "Ar user profile"


class ArUserProfilePermission(models.Model):
    profile_key = models.ForeignKey(ArUserProfile, on_delete=models.SET_NULL,   default="",null=True , related_name='userprofilepermission_by_userprofile')
    ORG_ID = models.ForeignKey(AR_organization, on_delete=models.SET_NULL,  default="",null=True , related_name='userprofilepermission_by_organization')
    ##################################################################
    activites = models.CharField(max_length=80)
    editor = models.BooleanField(default=False)
    viewer = models.BooleanField(default=False)
    ##############################################################
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='create_by_userprofilepermission',null=True )
    create_dt = models.DateTimeField(default=django.utils.timezone.now)
    update_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='update_by_userprofilepermission',null=True )
    update_dt = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.profile_key)
    class Meta:
        verbose_name_plural = "Ar user profile permission"

###############################################################


class Ar_user(models.Model):
    user = models.OneToOneField(User,  on_delete=models.SET_NULL, null=True, blank=True)
    user_name = models.CharField(max_length=50, default=None,blank=True)
    address = models.CharField(max_length=255, default="", blank=True)
    city = models.CharField(max_length=255, default="", blank=True)
    state = models.CharField(max_length=255, default="", blank=True)
    zip = models.IntegerField(default="", blank=True)
    country = models.CharField(max_length=50, default="", blank=True)
    phone = models.BigIntegerField(default="", blank=True)
    backup_email = models.EmailField(max_length=50, default="", blank=True)
    user_type = models.CharField(max_length=50, default="Root")
    subscription_level = models.CharField(max_length=50, default="Free trial")
    active_user = models.IntegerField(default=0)
    user_to_invite = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default="Active")
    # profile_permission = models.ForeignKey(ArUserProfile, on_delete=models.SET_NULL, null=True,  blank=True, related_name='user_favourite')
    profile_permission = models.ManyToManyField(ArUserProfile,blank=True, related_name='user_favourite')
    login_status = models.BooleanField(default=False)
    activate_status = models.BooleanField(default=False)
    terms_accept = models.BooleanField(default=True)
    org_id = models.ForeignKey(AR_organization, on_delete=models.SET_NULL,  default="",null=True ,  blank=True)
    verification_status = models.BooleanField(default=False)
    created_by = models.IntegerField(default=0)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.IntegerField(default=0)
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    data_Type = models.CharField(max_length=50, default="ORG Data",blank=True)
    def __str__(self):
        return str(self.user_name)
    class Meta:
        verbose_name_plural = "Ar user"

class ArShowcolumns(models.Model):
    Table_name = models.CharField(max_length=50)
    user = models.ForeignKey(Ar_user,on_delete=models.SET_NULL, null=True, blank=True)
    ORG = models.ForeignKey(AR_organization,  default="",null=True , on_delete=models.SET_NULL, blank=True)
    columnName = models.TextField()
    def _str__(self):
        return str(self.Table_name)
    class Meta:
        verbose_name_plural = "Ar show columns"

class csvFilesUplodaded(models.Model):
    attachments = models.FileField(upload_to='csvfileuplodaded/')
    csvUseFor = models.CharField(max_length=50)
    ORG_ID = models.ForeignKey(AR_organization, on_delete=models.SET_DEFAULT,  default="",null=True )
    created_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL, related_name='create_by_csvFilesUplodaded',null=True )
    updated_dt = models.DateTimeField(default=django.utils.timezone.now)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    updated_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL, related_name='update_by_csvFilesUplodaded',null=True )
    class Meta:
        verbose_name_plural = "CSV files uploaded"



class Notification(models.Model):
    page_name = models.CharField(max_length=50)
    notification_key = models.CharField(max_length=50)
    notification_desc = models.TextField()
    def _str__(self):
        return str(self.notification_desc)
    class Meta:
        verbose_name_plural = "Notification"


class ArUserStoryScoringPoints(models.Model):
    Score_for = models.CharField(max_length=50)
    Score_key = models.CharField(max_length=50)
    Keyword = models.TextField()
    Score_one = models.IntegerField(default=0)
    Score_two = models.IntegerField(default=0)
    Score_three = models.IntegerField(default=0)
    Last_Update = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.Score_key)
    class Meta:
        verbose_name_plural = "Ar user story scoring points"



class ArJobStoryScoringPoints(models.Model):
    Score_for = models.CharField(max_length=50)
    Score_key = models.CharField(max_length=50)
    Keyword = models.TextField()
    Score_one = models.IntegerField(default=0)
    Score_two = models.IntegerField(default=0)
    Score_three = models.IntegerField(default=0)
    Last_Update = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.Score_key)
    class Meta:
        verbose_name_plural = "Ar job story scoring points"


class ArTestStoryScoringPoints(models.Model):
    Score_for = models.CharField(max_length=50)
    Score_key = models.CharField(max_length=50)
    Keyword = models.TextField()
    Score_one = models.IntegerField(default=0)
    Score_two = models.IntegerField(default=0)
    Score_three = models.IntegerField(default=0)
    Last_Update = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return str(self.Score_key)
    class Meta:
        verbose_name_plural = "Ar test story scoring points"




class ArHelpContect(models.Model):
    Page_name = models.CharField(max_length = 50)
    Page_slug = models.CharField(max_length = 250, unique=True, null = True, blank = True,help_text="Copy URL after the "+settings.BASE_URL+" and past")
    Topic = models.CharField(max_length = 50)
    Description = models.TextField(default="Description")
    Information = models.TextField(default="Information.")
    Linke_1 = models.URLField(null = True, blank = True, default="http://203.190.153.20/")
    Linke_2 = models.URLField(null = True, blank = True, default="http://203.190.153.20/")
    Linke_3 = models.URLField(null = True, blank = True, default="http://203.190.153.20/")
    create_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Topic)
    class Meta:
        verbose_name_plural = "Ar help content"


class ArAccountRemoveRequest(models.Model):
    RootUser = models.CharField(max_length=50,default="")
    userEmail = models.CharField(max_length=50,default="")
    ORG_ID = models.ForeignKey(AR_organization ,related_name="account_remobe_org_id" ,default="" ,on_delete=models.SET_NULL, null=True, blank=True)
    Request_date = models.DateTimeField(default=django.utils.timezone.now)
    Request_Check = models.BooleanField(default=False)
    Account_activate = models.BooleanField(default=True)
    Account_Removed = models.BooleanField(default=False)
    Account_Removed_date = models.DateTimeField(null=True,blank=True)
    Account_deactivate_date = models.DateTimeField(null=True,blank=True)
    Remove_by = models.ForeignKey(User ,related_name="account_remobe_remove_by" ,default="" , on_delete=models.SET_NULL, null=True, blank=True)
    Mail_send_status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.RootUser)
    class Meta:
        verbose_name_plural = "Ar Account Remove Request"
