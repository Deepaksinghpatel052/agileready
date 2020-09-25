# Generated by Django 3.0.8 on 2020-08-04 09:58

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_backlogs', '0003_ar_backlog_backlog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ar_backlog',
            name='backlog_slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from='title', unique_with=('created_dt__month',)),
        ),
    ]