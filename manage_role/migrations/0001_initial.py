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
            name='ArRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('desc', models.TextField(blank=True)),
                ('use', models.TextField(blank=True, default='')),
                ('create_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_Type', models.CharField(blank=True, default='ORG Data', max_length=50)),
                ('ORG_ID', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.AR_organization')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_by_role', to='account.Ar_user')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_role', to='account.Ar_user')),
            ],
            options={
                'verbose_name_plural': 'Ar role',
            },
        ),
    ]