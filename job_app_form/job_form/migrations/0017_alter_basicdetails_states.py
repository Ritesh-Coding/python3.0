# Generated by Django 4.2.13 on 2024-06-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_form', '0016_alter_languageknown_language_known'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='states',
            field=models.CharField(choices=[], max_length=25),
        ),
    ]