# Generated by Django 4.2.13 on 2024-06-12 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_form', '0007_alter_languageknown_can_read_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageknown',
            name='language_known',
            field=models.CharField(choices=[('hindi', 'Hindi'), ('gujarati', 'Gujarati'), ('english', 'English')], default=None, max_length=15),
        ),
    ]
