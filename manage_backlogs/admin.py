from django.contrib import admin
from .models import AR_BACKLOG_STATUS,AR_BACKLOG
# Register your models here.

class AR_BACKLOG_STATUSAdmin(admin.ModelAdmin):
    search_fields = ['bl_status_key']
    list_display = ('bl_status_key','bl_status_desc')

class AR_BACKLOGAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title','owner','children_us_list')

admin.site.register(AR_BACKLOG_STATUS,AR_BACKLOG_STATUSAdmin)
admin.site.register(AR_BACKLOG,AR_BACKLOGAdmin)

