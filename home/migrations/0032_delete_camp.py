# Generated by Django 4.0.1 on 2022-03-30 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_rename_event_camp_alter_mailtext_attachment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Camp',
        ),
    ]