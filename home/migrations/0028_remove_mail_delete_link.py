# Generated by Django 4.0.1 on 2022-03-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_mailtext_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='delete_link',
        ),
    ]
