# Generated by Django 4.0.1 on 2022-03-31 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_remove_appointment_app_type_appointment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
    ]