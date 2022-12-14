# Generated by Django 4.0 on 2022-03-23 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agentDirectory', '0015_alter_agentdir_batch_id'),
        ('listing', '0016_alter_listing_rental_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='AgentCity_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='relatedCity', to='agentDirectory.agentcity'),
        ),
    ]
