# Generated by Django 4.0.1 on 2022-03-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(choices=[('A', 'accepted'), ('R', 'Rejected')], default=0),
        ),
    ]
