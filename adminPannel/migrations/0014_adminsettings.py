# Generated by Django 4.0 on 2022-02-25 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0013_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeSliderImage', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Home Slider Image')),
            ],
        ),
    ]
