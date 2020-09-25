# Generated by Django 3.0.8 on 2020-07-27 06:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArJobsitSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_product_list', models.CharField(blank=True, max_length=100, null=True)),
                ('jobsit_validation_list', models.TextField()),
                ('Use_in', models.TextField()),
                ('created_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('ORG_ID', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.AR_organization')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_by_ArJobsitSet', to='account.Ar_user')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_ArJobsitSet', to='account.Ar_user')),
            ],
            options={
                'verbose_name_plural': 'Ar Jobsit Set',
            },
        ),
    ]