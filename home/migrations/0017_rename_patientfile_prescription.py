# Generated by Django 4.0.1 on 2022-03-27 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_patientfile_details_patientfile_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PatientFile',
            new_name='prescription',
        ),
    ]
