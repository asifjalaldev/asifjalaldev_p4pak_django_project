# Generated by Django 4.0 on 2022-01-25 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0007_rename_prince_userservice_charges_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userservice',
            name='duration',
        ),
    ]
