from django.db import models

# Create your models here.
class StripeAccount(models.Model):
    STRIPE_SECRET_KEY = models.CharField(max_length=80)
    STRIPE_PUBLISHABLE_KEY = models.CharField(max_length=100)
    currency_type = models.CharField(max_length=100)
    Payment_Method = models.CharField(max_length=100,default="Stripe")

    class Meta:
        db_table = "Stripe Account"