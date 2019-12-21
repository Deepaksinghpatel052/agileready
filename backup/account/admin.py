from django.contrib import admin
from .models import Ar_user,AR_organization,AR_organization_status
# Register your models here.

class Ar_userAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['user_name']
    list_display = ('user_name','city','state','zip','country','phone','backup_email','user_type','login_status','created_dt')


class AR_organization_statusAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['status_key']
    list_display = ('status_key','created_dt','created_by')


class AR_organizationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['organization_name']
    list_display = ('organization_name','subscription_level','organization_status','created_by','created_dt')

admin.site.register(Ar_user,Ar_userAdmin)
admin.site.register(AR_organization,AR_organizationAdmin)
admin.site.register(AR_organization_status,AR_organization_statusAdmin)

