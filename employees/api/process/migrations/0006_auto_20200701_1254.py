# Generated by Django 3.0.7 on 2020-07-01 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0005_auto_20200701_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processmainid',
            name='main_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mdepts', to='process.Departments'),
        ),
    ]