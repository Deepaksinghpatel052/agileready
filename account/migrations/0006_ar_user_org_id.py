# Generated by Django 2.2.2 on 2019-12-19 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_ar_user_org_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ar_user',
            name='org_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='friendsStatus', to='account.AR_organization'),
        ),
    ]