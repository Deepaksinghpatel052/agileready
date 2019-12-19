# Generated by Django 2.2.2 on 2019-12-18 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ar_organization',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person2personsorganization', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ar_organization',
            name='organization_status',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.AR_organization_status'),
        ),
        migrations.AlterField(
            model_name='ar_organization',
            name='update_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='friendsorganization', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ar_organization_status',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person2personsstatuStatus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ar_organization_status',
            name='update_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='friendsStatus', to=settings.AUTH_USER_MODEL),
        ),
    ]
