from django.contrib import admin
from .models import AR_US_STATUS,AR_US_TYPE,AR_USER_STORY
# Register your models here.

class AR_US_STATUSAdmin(admin.ModelAdmin):
    search_fields = ['status_key']
    list_display = ('status_key','status_desc','status_shortcode')


class AR_US_TYPEAdmin(admin.ModelAdmin):
    search_fields = ['type_key']
    list_display = ('type_key','type_desc','type_short_code')


class AR_USER_STORYAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title','owner','story_tri_part_text','acceptance_criteria','ac_readability_score','conversation','convo_readability_score','autoscoring_on','archive_indicator','readiness_quality_score')


admin.site.register(AR_US_STATUS,AR_US_STATUSAdmin)
admin.site.register(AR_US_TYPE,AR_US_TYPEAdmin)
admin.site.register(AR_USER_STORY,AR_USER_STORYAdmin)
