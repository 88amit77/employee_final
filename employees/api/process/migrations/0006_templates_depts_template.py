# Generated by Django 3.0.7 on 2020-06-15 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0005_departments_templates'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates',
            name='depts_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='template_depts', to='process.Departments'),
        ),
    ]