# Generated by Django 4.0 on 2022-04-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_batch_id_profile_isgold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='bio'),
        ),
    ]
