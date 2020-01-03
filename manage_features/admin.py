from django.contrib import admin
from .models import AR_FEATURE
# Register your models here.

class AR_FEATUREYAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_dt'
    # search_fields = ['Cepic_key','ORG_ID']
    list_display = ('Feature_key','Feature_desc','CE_ID','ORG_ID','create_by','create_dt','update_by','update_dt')


admin.site.register(AR_FEATURE,AR_FEATUREYAdmin)
