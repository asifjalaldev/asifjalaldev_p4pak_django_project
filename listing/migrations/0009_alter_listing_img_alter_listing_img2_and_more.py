# Generated by Django 4.0 on 2022-02-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_alter_listing_img_alter_listing_img2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img',
            field=models.ImageField(blank=True, upload_to='static/images/listing_images', verbose_name='Image 1'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='img2',
            field=models.ImageField(blank=True, upload_to='static/images/listing_images', verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='img3',
            field=models.ImageField(blank=True, upload_to='static/images/listing_images', verbose_name='Image 3'),
        ),
    ]
