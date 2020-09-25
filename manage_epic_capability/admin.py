from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import AR_EPIC_CAPABILITY
# Register your models here.
class AR_EPIC_CAPABILITYAdmin(ImportExportModelAdmin):
# class AR_EPIC_CAPABILITYAdmin(SummernoteModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['Procduct_name','ORG_ID']
    # summernote_fields = ['Cepic_desc']
    # list_display = ('Cepic_key','Cepic_desc','ORG_ID','created_by','create_dt')
    list_display = ('Cepic_key','epic_capability_slug','ORG_ID','Cepic_desc','created_by','create_dt')

admin.site.register(AR_EPIC_CAPABILITY,AR_EPIC_CAPABILITYAdmin)
