from django.db import models
import django
from django.contrib.auth.models import User
from autoslug import AutoSlugField



# __________________________Table for Destination City_____________________________________
class Ar_Category(models.Model):
    name = models.CharField( unique=True,max_length=50)
    category_slug = AutoSlugField(populate_from='name', always_update=True, null=True,
                                 blank=True)

    created_dt = models.DateTimeField(default=django.utils.timezone.now)
    created_by = models.ForeignKey(User, related_name='category', on_delete=models.SET_NULL,null=True )
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "Category Table"
# _______________________________________________________________
