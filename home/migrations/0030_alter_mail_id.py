# Generated by Django 4.0.1 on 2022-03-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_mail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
