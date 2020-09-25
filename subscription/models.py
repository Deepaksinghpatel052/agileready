from django.db import models
from django.contrib.auth.models import User
from account.models import Ar_user,AR_organization
import django

# Create your models here.
class Subscription(models.Model):
	Title  = models.CharField(max_length=50,blank=True)
	Price = models.IntegerField(default=0,help_text="'0' Equal to 'Free'")
	Description = models.TextField(blank=True,help_text="Description about package.")
	All_member = models.BooleanField(default=False, blank=True,help_text="View for All Member.")
	Undefine_price = models.BooleanField(default=False,blank=True,help_text="Q3 2020")
	Active = models.BooleanField(default=False,blank=True)
	Role_access_and_security = models.BooleanField(default=False,blank=True)
	Invite_user  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Team  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Product  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Backlog_per_Product  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Rating_cycle  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	User_story  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Job_story  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Test_story  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Time_duration_count  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Time_duration_type  = models.CharField(max_length=50,default="Day")
	create_by = models.ForeignKey(User, on_delete=models.SET_NULL,default="",related_name='create_by_subscription',blank=True,null=True)
	create_dt = models.DateTimeField(default=django.utils.timezone.now)
	class Meta:
		verbose_name_plural = "AR Subscription"

	def __str__(self):
		return str(self.Title)


class MembershipHistory(models.Model):
	Package_name = models.ForeignKey(Subscription,on_delete=models.SET_NULL,default="",related_name='package_name_by_membership_history',blank=True,null=True)
	Organization = models.ForeignKey(AR_organization, on_delete=models.SET_NULL,default="",related_name='organization_by_membership_history',blank=True,null=True)
	Root_user = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,default="",related_name='root_user_by_membership_history',blank=True,null=True)
	Payment_Done = models.BooleanField(default=False,blank=True)
	Price = models.IntegerField(default=0,help_text="'0' Equal to 'Free'")
	Active = models.BooleanField(default=False,blank=True)
	Active_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	Role_access_and_security = models.BooleanField(default=False,blank=True)
	Invite_user  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Team  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Product  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Backlog_per_Product  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Rating_cycle  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	User_story  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Job_story  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Test_story  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Time_duration_count  = models.IntegerField(default=0,help_text="'0' Equal to 'Unlimited'")
	Time_duration_type  = models.CharField(max_length=50,default="Day")
	create_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,default="",related_name='create_by_membership_history',blank=True,null=True)
	create_dt = models.DateTimeField(default=django.utils.timezone.now)
	class Meta:
		verbose_name_plural = "AR Membership History"

	def __str__(self):
		return str(self.Package_name)	




class Payment(models.Model):
	payment_for = models.ForeignKey(MembershipHistory, on_delete=models.SET_NULL,default="",related_name='payment_id_by_payment',blank=True,null=True)
	Organization = models.ForeignKey(AR_organization, on_delete=models.SET_NULL,default="",related_name='organization_by_payment',blank=True,null=True)
	Root_user = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,default="",related_name='root_user_by_membership_payment',blank=True,null=True)
	Payment_method = models.CharField(max_length=80, default="")
	Payment_Done = models.BooleanField(default=False,blank=True)
	Currency_type = models.CharField(max_length=50, default="$")
	Amount = models.IntegerField(default=0,help_text="'0' Equal to 'Free'")
	payment_date = models.DateTimeField(default=django.utils.timezone.now)
	Transaction_id = models.CharField(max_length=150, default="")
	class Meta:
		verbose_name_plural = "AR Payment"

	def __str__(self):
		return str(self.Transaction_id)

class MembershipRequest(models.Model):
	Request_from = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,default="",related_name='Request_from_MembershipRequest',blank=True,null=True)
	Organization = models.ForeignKey(AR_organization, on_delete=models.SET_NULL,default="",related_name='Organization_MembershipRequest',blank=True,null=True)
	Request_for = models.CharField(max_length=50,blank=True,null=True)
	Request_done = models.BooleanField(default=False,blank=True)
	Description = models.TextField(blank=True,help_text="Description about request.")
	create_dt = models.DateTimeField(default=django.utils.timezone.now)
	class Meta:
		verbose_name_plural = "Membership Request"

	def __str__(self):
		return str(self.Description)

class MailForPaymentStatus(models.Model):
	payment_for = models.ForeignKey(Payment, on_delete=models.SET_NULL,default="",related_name='payment_id_by_payment',blank=True,null=True) 
	Organization = models.ForeignKey(AR_organization, on_delete=models.SET_NULL,default="",related_name='organization_for_mail',blank=True,null=True)
	Request_from = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,default="",related_name='Request_from_mail',blank=True,null=True)
	User_email = models.CharField(max_length=80, default="")
	create_date = 	models.DateTimeField(default=django.utils.timezone.now)
	send_status = models.BooleanField(default=False)
	send_date = models.DateTimeField(null=True, blank=True)

	class Meta:
		verbose_name_plural = "Mail For Payment Status"
	
	def __str__(self):
		return str(self.User_email)	