# Generated by Django 3.0.8 on 2020-08-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_jobmot_set', '0002_auto_20200731_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arjobmotset',
            name='member_product_list',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]