# Generated by Django 2.2.4 on 2020-01-04 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_key', models.CharField(blank=True, max_length=50)),
                ('create_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('ORG_ID', models.ForeignKey(on_delete='models.SET_NULL', related_name='userprofile_by_organization', to='account.AR_organization')),
                ('create_by', models.ForeignKey(on_delete='models.SET_NULL', related_name='create_by_userprofile', to='account.Ar_user')),
                ('update_by', models.ForeignKey(on_delete='models.SET_NULL', related_name='update_by_userprofile', to='account.Ar_user')),
            ],
        ),
        migrations.CreateModel(
            name='ArUserProfilePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activites', models.CharField(max_length=80)),
                ('editor', models.BooleanField(default=False)),
                ('viewer', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('ORG_ID', models.ForeignKey(on_delete='models.SET_NULL', related_name='userprofilepermission_by_organization', to='account.AR_organization')),
                ('create_by', models.ForeignKey(on_delete='models.SET_NULL', related_name='create_by_userprofilepermission', to='account.Ar_user')),
                ('profile_key', models.ForeignKey(on_delete='models.SET_NULL', related_name='userprofilepermission_by_userprofile', to='manage_user_profile.ArUserProfile')),
                ('update_by', models.ForeignKey(on_delete='models.SET_NULL', related_name='update_by_userprofilepermission', to='account.Ar_user')),
            ],
        ),
    ]
