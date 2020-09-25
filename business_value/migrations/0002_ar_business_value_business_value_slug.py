# Generated by Django 3.0.8 on 2020-08-04 11:52

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_value', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ar_business_value',
            name='business_value_slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from='bus_value_position', unique_with=('ORG_ID',)),
        ),
    ]
