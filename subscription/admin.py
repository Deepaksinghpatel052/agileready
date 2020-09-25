from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Subscription,Payment,MembershipHistory,MembershipRequest,MailForPaymentStatus
from account.models import Ar_user
from import_export.admin import ImportExportModelAdmin
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from agileproject import settings
from django.contrib.auth.models import User,auth
from agileproject.tokens import account_activation_token
import email.message
import smtplib
from django.template.loader import render_to_string
# Register your models here.

class SubscriptionAdmin(ImportExportModelAdmin):
    search_fields = ['Title']
    list_display = ('Title','Price','Undefine_price','Active','All_member','Role_access_and_security','Invite_user','Team','Product','Backlog_per_Product','Rating_cycle','User_story','Job_story','Test_story','Time_duration_count','Time_duration_type')

class MembershipRequestAdmin(ImportExportModelAdmin):
    search_fields = ['Request_done']
    list_display = ('Request_from','Organization','Request_for','Request_done','Description','create_dt')


class MembershipHistoryAdmin(ImportExportModelAdmin):
    search_fields = ['Package_name','Organization']
    list_display = ('Package_name','payment_link','Organization','Root_user','Payment_Done','Price','Active','Active_date','end_date','Role_access_and_security','Invite_user','Team','Product','Backlog_per_Product','Rating_cycle','User_story','Job_story','Test_story','Time_duration_count','Time_duration_type','create_by','create_dt')
    actions = {'send_payment_link',}





    def payment_link(self,membership):
        return "payment_link"


    def send_payment_link(self,request,queryset):
        default = "Test"
        count_get = queryset
        for item in count_get:
            if Ar_user.objects.filter(org_id=item.Organization).filter(user_type='Root').exists():
                get_root_user = get_object_or_404(Ar_user,org_id=item.Organization , user_type='Root')
                m_his = MembershipHistory.objects.filter(id=item.id).update(Price=item.Package_name.Price,Role_access_and_security=item.Package_name.Role_access_and_security,Invite_user=item.Package_name.Invite_user,Team=item.Package_name.Team,Product=item.Package_name.Product,Backlog_per_Product=item.Package_name.Backlog_per_Product,Rating_cycle=item.Package_name.Rating_cycle,User_story=item.Package_name.User_story,Job_story=item.Package_name.Job_story,Test_story=item.Package_name.Test_story,Time_duration_count=item.Package_name.Time_duration_count,Time_duration_type=item.Package_name.Time_duration_type)
                amount = urlsafe_base64_encode(force_bytes(item.Package_name.Price))
                package_id = urlsafe_base64_encode(force_bytes(item.id))
                payment_link = settings.BASE_URL+"subscription/"+str(amount)+"/"+package_id
                data_content = {"BASE_URL":settings.BASE_URL, "user_name":"Admin","logo_image":settings.BASE_URL+"static/img/basic/logo.png","get_data":item,"payment_link":payment_link}
                email_content = render_to_string('email_template/send_payment_link_template.html',data_content)
                msg = email.message.Message()
                msg['Subject'] = 'Payment Link'
                msg['From'] = settings.EMAIL_HOST_USER
                msg['To'] = get_root_user.user.username
                password = settings.EMAIL_HOST_PASSWORD
                msg.add_header('Content-Type', 'text/html')
                msg.set_payload(email_content)
                s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
                s.starttls()
                # Login Credentials for sending the mail
                s.login(msg['From'], password)
                s.sendmail(msg['From'], [msg['To']], msg.as_string())
                self.message_user(request,"payment link send. ")
            else:
                self.message_user(request,"Root User is not avelavel for "+str(item.Organization)+" organization.")    
    send_payment_link.short_description = 'Send payment link'



class PaymentAdmin(ImportExportModelAdmin):
    search_fields = ['Organization','Root_user','Transaction_id']
    list_display = ('payment_for','Organization','Root_user','Payment_method','Payment_Done','Amount','Currency_type','Transaction_id','payment_date')




class MailForPaymentStatusAdmin(ImportExportModelAdmin):
    search_fields = ['payment_for','Organization','User_email','Request_from']
    list_display = ('payment_for','Organization','Request_from','User_email','create_date','send_status','send_date')


admin.site.register(MailForPaymentStatus,MailForPaymentStatusAdmin)
admin.site.register(Subscription,SubscriptionAdmin)
admin.site.register(MembershipHistory,MembershipHistoryAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(MembershipRequest,MembershipRequestAdmin)