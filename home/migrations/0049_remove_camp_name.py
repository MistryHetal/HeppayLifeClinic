# Generated by Django 4.0.1 on 2022-04-23 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_camp_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='name',
        ),
    ]
