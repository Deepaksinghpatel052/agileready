from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ArRole
# Register your models here.

class ArRoleAdmin(ImportExportModelAdmin):
    list_display = ('role_id', 'title','desc','use','ORG_ID','create_by','create_dt','update_by','update_dt')
    list_filter = ('title', 'ORG_ID', 'create_by')

admin.site.register(ArRole,ArRoleAdmin)