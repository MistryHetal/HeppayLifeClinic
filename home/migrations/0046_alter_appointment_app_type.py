# Generated by Django 4.0.1 on 2022-03-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='app_type',
            field=models.CharField(choices=[('O', 'online'), ('F', 'Offline')], default='F', max_length=50),
        ),
    ]
