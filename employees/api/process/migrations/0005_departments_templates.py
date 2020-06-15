# Generated by Django 3.0.7 on 2020-06-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0004_connections_connection_process'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('template_id', models.AutoField(primary_key=True, serialize=False)),
                ('template_name', models.CharField(max_length=50)),
            ],
        ),
    ]
