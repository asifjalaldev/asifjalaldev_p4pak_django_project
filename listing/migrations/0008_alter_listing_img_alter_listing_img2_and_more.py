# Generated by Django 4.0 on 2022-02-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_alter_listing_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/listing_images', verbose_name='Image 1'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='img2',
            field=models.ImageField(blank=True, upload_to='images/listing_images', verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='img3',
            field=models.ImageField(blank=True, upload_to='images/listing_images', verbose_name='Image 3'),
        ),
    ]
