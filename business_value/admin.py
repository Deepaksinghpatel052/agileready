from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import AR_BUSINESS_VALUE

# Register your models here.

class AR_BUSINESS_VALUEAdmin(ImportExportModelAdmin):
    search_fields = ['bus_value_position','bus_value_txt_code','ORG_ID']
    list_display = ('bus_value_position','business_value_slug','bus_value_txt_code','bus_value_desc','ORG_ID')

admin.site.register(AR_BUSINESS_VALUE,AR_BUSINESS_VALUEAdmin)
