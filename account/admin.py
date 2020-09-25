from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group
from manage_iterations.models import ArIterations
from manage_features.models import AR_FEATURE
from user_story_view.models import AR_USER_STORY
from user_story_points.models import ArUserStoryPoints
from manage_role.models import ArRole
from manage_goals.models import ArManageGoals
from manage_benefits.models import ArManageBenefits
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_backlogs.models import AR_BACKLOG
from manage_product.models import AR_product,AR_team
from data_import_export.models import import_files_data 
from django.contrib.auth.models import User
from feedback.models import ArSendFeedbackEmail
import django
from account.models import csvFilesUplodaded,ArShowcolumns,ArUserProfilePermission,ArUserProfile,Ar_user,AR_organization
from subscription.models import MailForPaymentStatus,Payment,MembershipRequest,MembershipHistory
from .models import ArAccountRemoveRequest,Ar_user,AR_organization,AR_organization_status,ArShowcolumns,csvFilesUplodaded,ArUserProfile,ArUserProfilePermission,Notification,ArJobStoryScoringPoints,ArTestStoryScoringPoints,ArUserStoryScoringPoints,ArHelpContect
# Register your models here.



class Ar_userAdmin(ImportExportModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['user_name']
    list_display = ('user_name','city','state','zip','country','phone','backup_email','org_id','user_type','login_status','created_dt')


class AR_organization_statusAdmin(ImportExportModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['status_key']
    list_display = ('status_key','created_dt','created_by')


class AR_organizationAdmin(ImportExportModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['organization_name']
    list_display = ('organization_name','subscription_level','organization_status','Activate_status','created_by','created_dt')

class ArShowcolumnsAdmin(ImportExportModelAdmin):
    search_fields = ['user_id']
    list_display = ('user','ORG','Table_name','columnName')

class csvFilesUplodadedAdmin(ImportExportModelAdmin):
    search_fields = ['ORG_ID']
    list_display = ('attachments','csvUseFor','ORG_ID','created_by')
    list_filter = ('csvUseFor','created_by',)


class ArUserProfileAdmin(ImportExportModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['profile_key']
    list_display = ('profile_key','ORG_ID','create_by','create_dt','update_by','update_dt')

class ArUserProfilePermissionAdmin(ImportExportModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['profile_key']
    list_display = ('profile_key','ORG_ID','activites','editor','viewer','create_by','create_dt','update_by','update_dt')
    list_filter = ('profile_key', 'ORG_ID', 'activites')



class NotificationAdmin(ImportExportModelAdmin):
    search_fields = ['page_name','notification_desc']
    list_display = ('page_name','notification_key','notification_desc')
    list_filter = ('page_name','notification_key')

class ArUserStoryScoringPointsAdmin(ImportExportModelAdmin):
    search_fields = ['Score_for','Score_key']
    list_display = ('Score_for','Score_key','Keyword','Score_one','Score_two','Score_three','Last_Update')

class ArJobStoryScoringPointsAdmin(ImportExportModelAdmin):
    search_fields = ['Score_for','Score_key']
    list_display = ('Score_for','Score_key','Keyword','Score_one','Score_two','Score_three','Last_Update')

class ArTestStoryScoringPointsAdmin(ImportExportModelAdmin):
    search_fields = ['Score_for','Score_key']
    list_display = ('Score_for','Score_key','Keyword','Score_one','Score_two','Score_three','Last_Update')


class ArHelpContectAdmin(ImportExportModelAdmin):
    search_fields = ['Page_name','Topic']
    list_display = ('Page_name','Page_slug','Topic','Description','Information','Linke_1','Linke_2','Linke_3','create_dt')
    list_filter = ('Page_name', 'Page_slug','Topic')



class ArAccountRemoveRequestAdmin(ImportExportModelAdmin):
    search_fields = ['RootUser','ORG_ID']
    list_display = ('RootUser','userEmail','ORG_ID','Request_date','Request_Check','Account_Removed','Account_activate','Account_Removed_date','Account_deactivate_date','Remove_by','Mail_send_status')
    list_filter = ('ORG_ID', 'Request_Check','Account_Removed')
    actions = {'remove_add_data','accounts_deactivate','accounts_activate',}



    def accounts_activate(self,request,queryset):
        default = "Test"
        count_get = queryset
        for item in count_get:
            if item.ORG_ID:
                AR_organization.objects.filter(id=item.ORG_ID.id).update(Activate_status=True)
        count_get.update(Account_activate=True)        
        self.message_user(request,"Accountes are Activated.")  
    accounts_activate.short_description = 'Activate Accountes'

    def accounts_deactivate(self,request,queryset):
        default = "Test"
        count_get = queryset
        for item in count_get:
            if item.ORG_ID:
                AR_organization.objects.filter(id=item.ORG_ID.id).update(Activate_status=False)
        count_get.update(Request_Check=True,Account_activate=False,Account_deactivate_date=django.utils.timezone.now())        
        self.message_user(request,"Accountes are deactivated.")  
    accounts_deactivate.short_description = 'Deactivate Accountes'




    def remove_add_data(self,request,queryset):
        default = "Test"
        count_get = queryset
        for item in count_get:
            if item.ORG_ID:
                if ArIterations.objects.filter(ORG_ID=item.ORG_ID).exists():
                    ArIterations.objects.filter(ORG_ID=item.ORG_ID).delete()
                if AR_FEATURE.objects.filter(ORG_ID=item.ORG_ID).exists():
                    AR_FEATURE.objects.filter(ORG_ID=item.ORG_ID).delete()
                if AR_USER_STORY.objects.filter(ORG_id=item.ORG_ID).exists():
                    AR_USER_STORY.objects.filter(ORG_id=item.ORG_ID).delete() 
                if ArUserStoryPoints.objects.filter(ORG_ID=item.ORG_ID).exists():
                    ArUserStoryPoints.objects.filter(ORG_ID=item.ORG_ID).delete()
                if ArManageBenefits.objects.filter(ORG_ID=item.ORG_ID).exists():
                    ArManageBenefits.objects.filter(ORG_ID=item.ORG_ID).delete()                                       
                if ArManageGoals.objects.filter(ORG_ID=item.ORG_ID).exists():
                    ArManageGoals.objects.filter(ORG_ID=item.ORG_ID).delete()
                if ArRole.objects.filter(ORG_ID=item.ORG_ID).exists():
                    ArRole.objects.filter(ORG_ID=item.ORG_ID).delete()   
                if AR_EPIC_CAPABILITY.objects.filter(ORG_ID=item.ORG_ID).exists():
                    AR_EPIC_CAPABILITY.objects.filter(ORG_ID=item.ORG_ID).delete()    
                if AR_BACKLOG.objects.filter(ORG_ID=item.ORG_ID).exists():
                    AR_BACKLOG.objects.filter(ORG_ID=item.ORG_ID).delete()                                                            
                if AR_product.objects.filter(ORG_ID=item.ORG_ID).exists():
                    AR_product.objects.filter(ORG_ID=item.ORG_ID).delete() 
                if AR_team.objects.filter(ORG_id=item.ORG_ID).exists():
                    AR_team.objects.filter(ORG_id=item.ORG_ID).delete()  
                if csvFilesUplodaded.objects.filter(ORG_ID=item.ORG_ID).exists():
                    csvFilesUplodaded.objects.filter(ORG_ID=item.ORG_ID).delete()  
                if ArShowcolumns.objects.filter(ORG=item.ORG_ID).exists():
                    ArShowcolumns.objects.filter(ORG=item.ORG_ID).delete()   
                if ArUserProfilePermission.objects.filter(ORG_ID=item.ORG_ID).exists():
                    ArUserProfilePermission.objects.filter(ORG_ID=item.ORG_ID).delete()  
                if ArUserProfile.objects.filter(ORG_ID=item.ORG_ID).exists():
                    ArUserProfile.objects.filter(ORG_ID=item.ORG_ID).delete()                          
                if MailForPaymentStatus.objects.filter(Organization=item.ORG_ID).exists():
                    MailForPaymentStatus.objects.filter(Organization=item.ORG_ID).delete() 
                if Payment.objects.filter(Organization=item.ORG_ID).exists():
                    Payment.objects.filter(Organization=item.ORG_ID).delete() 
                if MembershipRequest.objects.filter(Organization=item.ORG_ID).exists():
                    MembershipRequest.objects.filter(Organization=item.ORG_ID).delete()  
                if MembershipHistory.objects.filter(Organization=item.ORG_ID).exists():
                    MembershipHistory.objects.filter(Organization=item.ORG_ID).delete() 
                if import_files_data.objects.filter(ORG_ID=item.ORG_ID).exists():
                    import_files_data.objects.filter(ORG_ID=item.ORG_ID).delete()                     
                set_flow = "0|"
                if Ar_user.objects.filter(org_id=item.ORG_ID).exists():            
                    get_all_user = Ar_user.objects.filter(org_id=item.ORG_ID)
                    for item2 in get_all_user:
                        if ArSendFeedbackEmail.objects.filter(user_id=item2).exists():
                            ArSendFeedbackEmail.objects.filter(user_id=item2).delete()
                        if item2.user is not None:
                            if User.objects.filter(id=item2.user.id).exists():
                                test = "sdkn"
                                User.objects.filter(id=item2.user.id).delete()
                    Ar_user.objects.filter(org_id=item.ORG_ID).delete()
                if AR_organization.objects.filter(organization_name=item.ORG_ID.organization_name).exists():
                    AR_organization.objects.filter(organization_name=item.ORG_ID.organization_name).delete() 
            count_get.update(Request_Check=True,Account_Removed=True,Account_Removed_date=django.utils.timezone.now())        
            self.message_user(request,"All data are removed")  
    remove_add_data.short_description = 'Remov all data'



admin.site.site_header = 'Agileready admin console'
admin.site.site_title = 'Agileready admin console'
admin.site.index_title = 'Agileready administration'


admin.site.unregister(Group)


admin.site.register(ArUserProfilePermission,ArUserProfilePermissionAdmin)
admin.site.register(ArUserProfile,ArUserProfileAdmin)
admin.site.register(Ar_user,Ar_userAdmin)
admin.site.register(AR_organization,AR_organizationAdmin)
admin.site.register(AR_organization_status,AR_organization_statusAdmin)
admin.site.register(ArShowcolumns,ArShowcolumnsAdmin)
admin.site.register(csvFilesUplodaded,csvFilesUplodadedAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(ArUserStoryScoringPoints,ArUserStoryScoringPointsAdmin)
admin.site.register(ArJobStoryScoringPoints,ArJobStoryScoringPointsAdmin)
admin.site.register(ArTestStoryScoringPoints,ArTestStoryScoringPointsAdmin)
admin.site.register(ArHelpContect,ArHelpContectAdmin)
admin.site.register(ArAccountRemoveRequest,ArAccountRemoveRequestAdmin)
