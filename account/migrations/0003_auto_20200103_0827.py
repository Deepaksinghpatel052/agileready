# Generated by Django 2.2.2 on 2020-01-03 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_arshowcolumns'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arshowcolumns',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='arshowcolumns',
            name='ORG',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.AR_organization'),
        ),
    ]