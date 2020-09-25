from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AR_product,AR_team
# Register your models here.

class Ar_productAdmin(ImportExportModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['Product_name','ORG_ID']
    list_display = ('Product_name','product_slug','Product_size','Product_score','US_quality_threshold','ORG_ID','create_by','create_dt')


class Ar_teamAdmin(ImportExportModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['Team_name','ORG_id']
    list_display = ('Team_name','Team_description','team_slug','ORG_id','create_by','update_by','update_by','create_dt',)
    list_filter = ('ORG_id',)
admin.site.register(AR_product,Ar_productAdmin)
admin.site.register(AR_team,Ar_teamAdmin)