# Generated by Django 4.0.1 on 2022-03-31 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_event_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]