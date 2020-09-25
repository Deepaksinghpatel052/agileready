from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Ar_Category


# Register your models here.

class Ar_Category_Admin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ('name','category_slug','created_dt','created_by')


admin.site.register(Ar_Category,Ar_Category_Admin)

