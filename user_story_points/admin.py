from django.contrib import admin
from .models import ArUserStoryPoints
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ArUserStoryPointsAdmin(ImportExportModelAdmin):
    date_hierarchy = 'create_dt'
    list_display = ('Point_Key','Point_Description','Point_score','ORG_ID','create_by','create_dt','update_by','update_dt')
    list_filter = ('Point_Key', 'ORG_ID')
admin.site.register(ArUserStoryPoints,ArUserStoryPointsAdmin)