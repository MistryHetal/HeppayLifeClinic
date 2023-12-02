# Generated by Django 4.0.1 on 2022-03-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='Type Patient Email..', max_length=50)),
                ('message', models.CharField(default='Type Patient Email..', max_length=50)),
                ('attachment', models.FileField(upload_to='')),
                ('send_it', models.BooleanField(default=False)),
                ('users', models.ManyToManyField(to='home.Mail')),
            ],
            options={
                'verbose_name': 'Emails to send',
                'verbose_name_plural': 'Emails to send',
            },
        ),
    ]
