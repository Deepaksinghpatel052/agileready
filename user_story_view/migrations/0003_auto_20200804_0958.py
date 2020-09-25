# Generated by Django 3.0.8 on 2020-08-04 09:58

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_story_view', '0002_ar_user_story_user_story_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ar_user_story',
            name='user_story_slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from='title', unique_with=('created_dt__month',)),
        ),
    ]