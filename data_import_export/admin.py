from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import export_data_info,import_files_data,demo_data_csv_template
# Register your models here.

class export_data_infoAdmin(admin.ModelAdmin):
    search_fields = ['Score_for','Score_key']
    list_display = ('folder_name','files_name','created_dt')


class import_dataAdmin(ImportExportModelAdmin):
    date_hierarchy = 'created_date'
    search_fields = ['files']
    list_display = ('file_name','files','file_data','error_log','upload_status','ORG_ID','created_by','created_date','priority','dommy_set')
    list_filter = ('file_name', 'ORG_ID', 'priority','dommy_set','created_by',)


class dommy_dataAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    search_fields = ['files']
    list_display = ('file_name','files','file_data','created_date','priority')
    list_filter = ('file_name','priority')

admin.site.register(export_data_info,export_data_infoAdmin)
admin.site.register(import_files_data,import_dataAdmin)
admin.site.register(demo_data_csv_template,dommy_dataAdmin)

