# Generated by Django 4.2.6 on 2023-12-06 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_schedule_bus_remove_schedule_route_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='route',
            name='schedule',
        ),
    ]
