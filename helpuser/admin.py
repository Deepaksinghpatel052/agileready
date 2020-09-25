from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Cms_manage
# Register your models here.

class Cms_manageAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['keyword','title']
    list_display = ('keyword','title','created_by','created_dt','updated_by','updated_dt')

admin.site.register(Cms_manage,Cms_manageAdmin)