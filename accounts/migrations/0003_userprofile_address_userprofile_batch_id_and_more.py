# Generated by Django 4.0 on 2022-04-26 05:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agentDirectory', '0017_alter_agentdir_batch_id'),
        ('accounts', '0002_alter_userprofile_website_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=230),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='batch_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agentBadge', to='agentDirectory.batch'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fullName',
            field=models.CharField(blank=True, max_length=130),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='joiningDate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profilePhoto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='profilePhoto size(width=220px, height=220px)'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website_url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
