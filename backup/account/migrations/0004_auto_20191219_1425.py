# Generated by Django 2.2.2 on 2019-12-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191219_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ar_user',
            name='org_id',
            field=models.CharField(default=0, max_length=50),
        ),
    ]