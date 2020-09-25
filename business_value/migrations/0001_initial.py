# Generated by Django 3.0.8 on 2020-07-27 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AR_BUSINESS_VALUE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_value_position', models.BigIntegerField(blank=True)),
                ('bus_value_txt_code', models.CharField(blank=True, default='', max_length=50)),
                ('bus_value_desc', models.TextField(blank=True, default='')),
                ('ORG_ID', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.AR_organization')),
            ],
            options={
                'verbose_name_plural': 'Ar Business Value',
            },
        ),
    ]
