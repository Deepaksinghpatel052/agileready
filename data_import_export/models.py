from django.db import models
from account.models import Ar_user,AR_organization
import django
# Create your models here.

class export_data_info(models.Model):
    folder_name = models.CharField(max_length=50)
    files_name = models.TextField(blank=True)
    created_dt = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.folder_name
    class Meta:
        verbose_name_plural = "Export data info"

class import_files_data(models.Model):
    files = models.FileField(upload_to='implode_data/')
    file_name = models.CharField(max_length=50)
    file_data = models.TextField()
    upload_status = models.BooleanField(default=False)
    error_log = models.FileField(upload_to='implode_data/error_log' ,default="None",blank=True,null=True)
    ORG_ID = models.ForeignKey(AR_organization,  default="",null=True ,blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(Ar_user, on_delete=models.SET_NULL,related_name='create_by_import_data',null=True ,blank=True, )
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    priority = models.IntegerField(default=0)
    dommy_set = models.IntegerField(default=0)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name_plural = "Import files data (Default data)"

class demo_data_csv_template(models.Model):
    files = models.FileField(upload_to='implode_data/')
    file_name = models.CharField(max_length=50)
    file_data = models.TextField(max_length=50)
    upload_status = models.BooleanField(default=False)
    error_log = models.FileField(upload_to='implode_data/error_log' ,default="None",blank=True,null=True)
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.file_name


    class Meta:
        verbose_name_plural = "Demo data csv template"