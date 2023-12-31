# Generated by Django 4.2.6 on 2023-11-14 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
                ('last_maintenance_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_point', models.CharField(max_length=100)),
                ('end_point', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('schedule', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bus')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.passenger')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.route')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=20)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bus')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='main.route')),
            ],
        ),
    ]
