# Generated by Django 2.2.2 on 2019-12-19 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191219_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ar_user',
            name='set_status_set',
        ),
    ]