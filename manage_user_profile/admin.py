from django.contrib import admin
from .models import ArUserProfile,ArUserProfilePermission

# Register your models here.

class ArUserProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['profile_key']
    list_display = ('profile_key','ORG_ID','create_by','create_dt','update_by','update_dt')

class ArUserProfilePermissionAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_dt'
    search_fields = ['profile_key']
    list_display = ('profile_key','ORG_ID','activites','editor','viewer','create_by','create_dt','update_by','update_dt')

admin.site.register(ArUserProfilePermission,ArUserProfilePermissionAdmin)