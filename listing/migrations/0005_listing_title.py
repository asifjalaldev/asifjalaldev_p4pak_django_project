# Generated by Django 4.0 on 2022-02-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0004_alter_listing_bathroom_alter_listing_bedroom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(blank=True, max_length=120, verbose_name='Purpose(title of propertity)'),
        ),
    ]
