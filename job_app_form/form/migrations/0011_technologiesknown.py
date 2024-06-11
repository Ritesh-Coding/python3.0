# Generated by Django 4.2.13 on 2024-06-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_alter_basicdetails_relationship_languageknown'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologiesKnown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technologies_known', models.CharField(choices=[('php', 'PHP'), ('mysql', 'MYSQL'), ('laravel', 'LARAVEL'), ('oracle', 'ORACLE')], max_length=15)),
                ('level_of_expertise', models.CharField(choices=[(1, 'Begineer'), (2, 'Mediator'), (3, 'Expertise')], default=None, max_length=9)),
                ('employee_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='form.basicdetails')),
            ],
        ),
    ]
