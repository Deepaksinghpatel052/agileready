from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ArJoboutcSet
# Register your models here.

class ArJoboutcSetAdmin(ImportExportModelAdmin):
    list_display = ('member_product_list', 'joboutc_validation_list','Use_in','ORG_ID','created_by','created_dt','updated_by','updated_dt')
    list_filter = ('member_product_list', 'ORG_ID', 'created_by')

admin.site.register(ArJoboutcSet,ArJoboutcSetAdmin)