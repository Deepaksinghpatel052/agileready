from django.contrib import admin
from .models import AR_EPIC_CAPABILITY
# Register your models here.
class AR_EPIC_CAPABILITYAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['Procduct_name','ORG_ID']
    list_display = ('Cepic_key','Cepic_desc','PROJECT_ID','ORG_ID','created_by','create_dt')

admin.site.register(AR_EPIC_CAPABILITY,AR_EPIC_CAPABILITYAdmin)
