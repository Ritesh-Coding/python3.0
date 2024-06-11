# Generated by Django 4.2.13 on 2024-06-07 07:49

import django.core.validators
from django.db import migrations, models
import form.models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Enter a valid First name.', regex='^[a-zA-Z\\s-]+$')])),
                ('lastName', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Enter a valid Last name.', regex='^[a-zA-Z\\s-]+$')])),
                ('designation', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Enter a valid Last name.', regex='^[a-zA-Z\\s-]+$')])),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(validators=[form.models.validate_phone])),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('states', models.CharField(max_length=10)),
                ('zip', models.IntegerField(validators=[form.models.validate_zip])),
                ('relationship', models.CharField(choices=[('single', 'SINGLE'), ('married', 'Married')], max_length=8)),
                ('date_of_birth', models.TextField(validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Enter a valid Date of Birth.', regex='/([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))/')])),
            ],
        ),
    ]
