# Generated by Django 4.0 on 2022-03-09 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0016_adminsettings_homesliderimage1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminsettings',
            name='homeSliderImage2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Home Image 3(size: width=2000px, hight=1000)'),
        ),
        migrations.AlterField(
            model_name='adminsettings',
            name='homeSliderImage1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Home Image 2(size: width=2000px, hight=1000)'),
        ),
    ]
