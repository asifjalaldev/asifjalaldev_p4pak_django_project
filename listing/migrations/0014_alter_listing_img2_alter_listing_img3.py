# Generated by Django 4.0 on 2022-02-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0013_alter_listing_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/listing_images', verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/listing_images', verbose_name='Image 3'),
        ),
    ]