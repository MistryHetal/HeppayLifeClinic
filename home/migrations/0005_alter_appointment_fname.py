# Generated by Django 4.0.1 on 2022-03-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='fname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
