from django.db import models
from datetime import datetime
import django
from user_story_view.models import AR_USER_STORY


# Create your models here.
# class AR_US_TYPE(models.Model):
#     type_key  = models.CharField(max_length=50,blank=True)
#     type_desc  = models.TextField(blank=True)
#     type_short_code   = models.CharField(max_length=50,blank=True)
#     create_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='create_by_us_type')
#     create_dt = models.DateTimeField(default=django.utils.timezone.now)
#     update_by = models.ForeignKey(Ar_user, on_delete='models.SET_NULL',related_name='update_by_us_type')
#     update_dt = models.DateTimeField(default=django.utils.timezone.now)
#
#     def __str__(self):
#         return str(self.type_key)
