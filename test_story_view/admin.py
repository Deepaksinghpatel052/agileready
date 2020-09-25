from django.contrib import admin
from .models import AR_TEST_STORY,test_story_file_attachment
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AR_TEST_STORYAdmin(ImportExportModelAdmin):
    search_fields = ['title']
    list_display = ('title','owner','BV_ID','product_parent','scenario_parent','story_tri_part_text','acceptance_criteria','ac_readability_score','conversation','convo_readability_score','autoscoring_on','archive_indicator','readiness_quality_score','created_by','updated_by','ORG_id')

admin.site.register(AR_TEST_STORY,AR_TEST_STORYAdmin)



class test_story_file_attachmentAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ('name','attachment','test_story')

admin.site.register(test_story_file_attachment,test_story_file_attachmentAdmin)