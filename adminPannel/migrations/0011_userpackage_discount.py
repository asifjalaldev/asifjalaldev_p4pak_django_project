# Generated by Django 4.0 on 2022-01-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0010_remove_services_offer_duration_useroffer_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpackage',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
