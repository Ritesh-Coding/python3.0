# Generated by Django 4.2.13 on 2024-06-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_form', '0012_rename_state_city_master_statecitymaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='cities',
            field=models.CharField(default='Ahmedabad', max_length=20),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='states',
            field=models.CharField(max_length=25),
        ),
    ]