# Generated by Django 4.0 on 2022-02-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentDirectory', '0007_agentdir_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentdir',
            name='isFeatured',
            field=models.BooleanField(default=False),
        ),
    ]
