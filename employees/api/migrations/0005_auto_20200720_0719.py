# Generated by Django 3.0.7 on 2020-07-20 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200713_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendenceleaveid',
            name='emp_id',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Employee'),
        ),
        migrations.AlterField(
            model_name='empleaveid',
            name='emp_id',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Employee'),
        ),
        migrations.AlterField(
            model_name='monthlyempsalary',
            name='month',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='designation',
            field=models.CharField(max_length=100),
        ),
    ]
