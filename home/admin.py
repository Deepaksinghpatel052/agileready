from django.contrib import admin
from .models import StripeAccount
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class SubscriptionAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ('STRIPE_SECRET_KEY','STRIPE_PUBLISHABLE_KEY','currency_type','Payment_Method')

admin.site.register(StripeAccount,SubscriptionAdmin)
