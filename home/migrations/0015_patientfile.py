# Generated by Django 4.0.1 on 2022-03-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
