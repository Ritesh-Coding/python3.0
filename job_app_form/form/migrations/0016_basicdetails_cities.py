# Generated by Django 4.2.13 on 2024-06-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0015_basicdetails_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicdetails',
            name='cities',
            field=models.CharField(default='Ahmedabad', max_length=15),
        ),
    ]
