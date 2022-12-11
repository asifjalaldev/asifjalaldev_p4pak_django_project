# Generated by Django 4.0 on 2022-02-18 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agentDirectory', '0007_agentdir_status'),
        ('listing', '0010_listing_isfeatured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='city',
        ),
        migrations.AddField(
            model_name='listing',
            name='AgentCity_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agentDirectory.agentcity'),
        ),
    ]