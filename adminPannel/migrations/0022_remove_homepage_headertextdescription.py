# Generated by Django 4.0 on 2022-04-08 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0021_homepage_headertextdescription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='headerTextDescription',
        ),
    ]
