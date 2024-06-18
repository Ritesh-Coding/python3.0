# Generated by Django 4.2.13 on 2024-06-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_form', '0015_alter_basicdetails_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageknown',
            name='language_known',
            field=models.CharField(blank=True, choices=[('hindi', 'Hindi'), ('gujarati', 'Gujarati'), ('english', 'English')], max_length=15, null=True),
        ),
    ]