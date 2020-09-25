from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AR_SCENARIO
# Register your models here.

class AR_SCENARIOAdmin(ImportExportModelAdmin):
    list_display = ('scenario_name', 'scenario_desc','product_id','created_by','created_dt','updated_by','updated_dt','ORG_ID')
    # list_filter = ('Benefits_title', 'ORG_ID', 'created_by')

admin.site.register(AR_SCENARIO,AR_SCENARIOAdmin)