# Generated by Django 4.2.13 on 2024-06-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0011_technologiesknown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologiesknown',
            name='level_of_expertise',
            field=models.CharField(choices=[('beginner', 'Begineer'), ('mediator', 'Mediator'), ('expertise', 'Expertise')], default=None, max_length=9),
        ),
    ]
