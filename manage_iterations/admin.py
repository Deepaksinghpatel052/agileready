from django.contrib import admin
from .models import ArIterations
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class ArIterationsAdmin(ImportExportModelAdmin):
    search_fields = ['IterationName']
    list_display = ('IterationName','iteration_slug','owner','IterationId','StartDate','EndDate','Product','Backlog','Team','IterationScore','IterationSize')


admin.site.register(ArIterations,ArIterationsAdmin)