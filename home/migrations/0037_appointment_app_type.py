# Generated by Django 4.0.1 on 2022-03-31 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_rename_date_feedback_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='app_type',
            field=models.CharField(choices=[('O', 'online'), ('F', 'Offline')], default='F', max_length=5),
        ),
    ]
