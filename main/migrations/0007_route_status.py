# Generated by Django 4.2.6 on 2023-12-16 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_ticket_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='status',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
