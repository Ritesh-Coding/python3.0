# Generated by Django 4.2.13 on 2024-06-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_form', '0014_alter_basicdetails_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='cities',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
