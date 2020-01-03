# Generated by Django 2.2.2 on 2020-01-03 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('manage_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AR_EPIC_CAPABILITY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cepic_key', models.CharField(max_length=50)),
                ('Cepic_desc', models.TextField()),
                ('Children_feature_list', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('create_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('ORG_ID', models.ForeignKey(on_delete='models.SET_NULL', to='account.AR_organization')),
                ('PROJECT_ID', models.ForeignKey(blank=True, default='', null=True, on_delete='models.SET_NULL', to='manage_product.AR_product')),
                ('created_by', models.ForeignKey(on_delete='models.SET_NULL', related_name='create_by_epic', to='account.Ar_user')),
                ('update_by', models.ForeignKey(on_delete='models.SET_NULL', related_name='update_by_epic', to='account.Ar_user')),
            ],
        ),
    ]
