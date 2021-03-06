from django.contrib import admin
from .models import AR_product,AR_team
# Register your models here.

class Ar_productAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['Procduct_name','ORG_ID']
    list_display = ('Procduct_name','Product_size','Product_score','US_quality_threshold','ORG_ID','create_by','create_dt')

admin.site.register(AR_product,Ar_productAdmin)
admin.site.register(AR_team)