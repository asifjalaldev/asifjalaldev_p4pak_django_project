# Generated by Django 4.0 on 2022-03-11 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agentDirectory', '0014_batch_remove_agentdir_batch_agentdir_batch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentdir',
            name='batch_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agentDirectory.batch'),
        ),
    ]
