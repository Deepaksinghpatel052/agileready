from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import ArFeedback, ArSendFeedbackEmail,ArAcadenyEmailForRecavedEmail,ArEmailSendToAdmin
# Register your models here.

class ArFeedbackAdmin(ImportExportModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['feedback_nature','page_name']
    list_display = ('page_name','feedback_nature','feedback_information','attachments','created_by','created_dt')
admin.site.register(ArFeedback,ArFeedbackAdmin)


class ArSendFeedbackEmailAdmin(ImportExportModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['page_name']
    list_display = ('page_name','feedback_id','user_id','status','sent_date','created_dt')
admin.site.register(ArSendFeedbackEmail,ArSendFeedbackEmailAdmin)

class ArAcadenyEmailForRecavedEmailAdmin(ImportExportModelAdmin):
    list_display = ('Email','Status')
admin.site.register(ArAcadenyEmailForRecavedEmail,ArAcadenyEmailForRecavedEmailAdmin)


class ArEmailSendToAdminAdmin(ImportExportModelAdmin):
    list_display = ('User_Email','Email_Subjects','Ar_user','ORG_ID','invited_by','Subscription_Plan','Mail_send','Mail_send_date','created_dt')
admin.site.register(ArEmailSendToAdmin,ArEmailSendToAdminAdmin)