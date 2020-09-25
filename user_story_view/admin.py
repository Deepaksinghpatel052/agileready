from django.contrib import admin
from .models import AR_US_STATUS,AR_US_TYPE,AR_USER_STORY,file_attachment,Help_Text
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AR_US_STATUSAdmin(ImportExportModelAdmin):
    search_fields = ['status_key']
    list_display = ('status_key','user_status_slug','status_desc','status_shortcode')

class file_attachmentAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ('name','attachment','user_story')

class AR_US_TYPEAdmin(ImportExportModelAdmin):
    search_fields = ['type_key']
    list_display = ('type_key','user_type_slug','type_desc','type_short_code')


class Help_TextAdmin(ImportExportModelAdmin):
    search_fields = ['page_name']
    list_display = ('page_name','page_slug','topic','description','information')


class AR_USER_STORYAdmin(ImportExportModelAdmin):
    search_fields = ['title']
    # list_display = ('title','owner','backlog_parent','BV_ID','user_story_slug','created_by','ORG_id')
    list_display = ('title','owner','story_tri_part_text','user_story_slug','acceptance_criteria','ac_readability_score','conversation','convo_readability_score','autoscoring_on','archive_indicator','readiness_quality_score','created_by','updated_by','ORG_id')

admin.site.register(file_attachment,file_attachmentAdmin)
admin.site.register(AR_US_STATUS,AR_US_STATUSAdmin)
admin.site.register(AR_US_TYPE,AR_US_TYPEAdmin)
admin.site.register(AR_USER_STORY,AR_USER_STORYAdmin)
admin.site.register(Help_Text,Help_TextAdmin)
