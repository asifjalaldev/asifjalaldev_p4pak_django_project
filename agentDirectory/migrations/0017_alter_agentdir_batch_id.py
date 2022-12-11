# Generated by Django 4.0 on 2022-04-05 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agentDirectory', '0016_alter_agentdir_agentcity_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentdir',
            name='batch_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='relatedBadge', to='agentDirectory.batch'),
        ),
    ]
