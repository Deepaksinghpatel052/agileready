from django.contrib import admin
from .models import AR_ITERATIONS
# Register your models here.
class AR_ITERATIONSAdmin(admin.ModelAdmin):
    search_fields = ['Iteration_key']
    list_display = ('Iteration_key','Assoc_us_list','owner','TM_ID')


admin.site.register(AR_ITERATIONS,AR_ITERATIONSAdmin)