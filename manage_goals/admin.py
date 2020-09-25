from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ArManageGoals
# Register your models here.

class ArManageGoalsAdmin(ImportExportModelAdmin):
    search_fields = ['bl_status_key']
    list_display = ('Goal_id', 'Goal_title','Gole_description','Use_in','ORG_ID','created_by','created_dt','updated_by','updated_dt')
    list_filter = ('Goal_title', 'ORG_ID', 'created_by')

admin.site.register(ArManageGoals,ArManageGoalsAdmin)