# Generated by Django 4.0 on 2022-03-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0018_remove_adminsettings_homesliderimage1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminsettings',
            name='midBanner',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='sideBanner size(width=750px, height=150px'),
        ),
        migrations.AddField(
            model_name='adminsettings',
            name='sideBanner',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='sideBanner size(width=700px, height=1500px'),
        ),
    ]