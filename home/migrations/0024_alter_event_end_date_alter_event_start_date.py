# Generated by Django 4.0.1 on 2022-03-28 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_event_event_check_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True, help_text='DD-MM-YYYY', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, help_text='DD-MM-YYYY', null=True),
        ),
    ]