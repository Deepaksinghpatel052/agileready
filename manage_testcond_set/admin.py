from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ArTestcondSet
# Register your models here.

class ArTestcondSetAdmin(ImportExportModelAdmin):
    list_display = ('member_product_list', 'member_scenario_list','Use_in','testcond_validation_list','ORG_ID','created_by','created_dt','updated_by','updated_dt')
    list_filter = ('member_product_list', 'ORG_ID', 'created_by')

admin.site.register(ArTestcondSet,ArTestcondSetAdmin)