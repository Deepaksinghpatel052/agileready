from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AR_BACKLOG_STATUS,AR_BACKLOG
# Register your models here.

class AR_BACKLOG_STATUSAdmin(ImportExportModelAdmin):
    search_fields = ['bl_status_key']
    list_display = ('bl_status_key','bl_status_desc')

class AR_BACKLOGAdmin(ImportExportModelAdmin):
    search_fields = ['title']
    list_display = ('title','backlog_description','owner','backlog_score','Backlog_size','backlog_slug','ORG_ID','product_parent')
    list_filter = ('ORG_ID','product_parent',)




admin.site.register(AR_BACKLOG_STATUS,AR_BACKLOG_STATUSAdmin)
admin.site.register(AR_BACKLOG,AR_BACKLOGAdmin)


