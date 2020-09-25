# Generated by Django 3.0.8 on 2020-08-04 13:53

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_iterations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ariterations',
            name='iteration_slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from='IterationName', unique_with=('create_dt__month',)),
        ),
    ]
