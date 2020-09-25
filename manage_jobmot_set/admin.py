from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ArJobmotSet
# Register your models here.

class ArJobmotSetAdmin(ImportExportModelAdmin):
    list_display = ('member_product_list', 'jobmot_validation_list','Use_in','ORG_ID','created_by','created_dt','updated_by','updated_dt')
    list_filter = ('member_product_list', 'created_by', 'ORG_ID')

admin.site.register(ArJobmotSet,ArJobmotSetAdmin)