# Generated by Django 4.0.1 on 2022-03-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_event_end_date_alter_event_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailtext',
            old_name='Users',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='app_type',
        ),
        migrations.AlterField(
            model_name='mailtext',
            name='attachment',
            field=models.CharField(default='Type prescription details', max_length=50),
        ),
    ]
