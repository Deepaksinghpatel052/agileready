from django.contrib import admin
from .models import AR_JOB_STORY,job_story_file_attachment
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AR_JOB_STORYAdmin(ImportExportModelAdmin):
    search_fields = ['title']
    list_display = ('title','owner','BV_ID','backlog_parent','story_tri_part_text','acceptance_criteria','ac_readability_score','conversation','convo_readability_score','autoscoring_on','archive_indicator','readiness_quality_score','created_by','updated_by','ORG_id')

admin.site.register(AR_JOB_STORY,AR_JOB_STORYAdmin)



class job_story_file_attachmentAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ('name','attachment','job_story')

admin.site.register(job_story_file_attachment,job_story_file_attachmentAdmin)