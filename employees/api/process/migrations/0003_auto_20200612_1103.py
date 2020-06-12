# Generated by Django 3.0.7 on 2020-06-12 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_auto_20200612_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='process_training',
            field=models.FileField(blank=True, null=True, upload_to='dropbox/videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm'])]),
        ),
        migrations.AlterField(
            model_name='processmainid',
            name='main_attachment',
            field=models.FileField(blank=True, null=True, upload_to='dropbox/videos_main', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'png', 'jpeg', 'jpg'])]),
        ),
        migrations.AlterField(
            model_name='processsubpoint',
            name='subpoint_attachment',
            field=models.FileField(blank=True, null=True, upload_to='dropbox/videos_subprocess', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'png', 'jpeg', 'jpg'])]),
        ),
    ]