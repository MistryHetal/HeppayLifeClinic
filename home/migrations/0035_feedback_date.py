# Generated by Django 4.0.1 on 2022-03-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_rename_users_mailtext_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(auto_now_add=True, help_text='DD-MM-YYYY', null=True),
        ),
    ]