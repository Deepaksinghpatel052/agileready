from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ArTestactSet
# Register your models here.

class ArTestactSetAdmin(ImportExportModelAdmin):
    list_display = ('member_product_list', 'member_scenario_list','testact_validation','Use_in','ORG_ID','created_by','created_dt','updated_by','updated_dt')
    list_filter = ('member_product_list', 'ORG_ID', 'created_by')

admin.site.register(ArTestactSet,ArTestactSetAdmin)