# Generated by Django 4.0 on 2022-01-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='img2',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='listing',
            name='img3',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='img',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
