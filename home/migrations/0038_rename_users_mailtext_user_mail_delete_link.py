# Generated by Django 4.0.1 on 2022-03-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_appointment_app_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailtext',
            old_name='users',
            new_name='user',
        ),
        migrations.AddField(
            model_name='mail',
            name='delete_link',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
