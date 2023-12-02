# Generated by Django 4.0.1 on 2022-03-31 07:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0038_rename_users_mailtext_user_mail_delete_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='Type Patient Email..', max_length=50)),
                ('message', models.CharField(default='Type Patient Email..', max_length=50)),
                ('attachment', models.CharField(default='Type Patient prescription..', max_length=250)),
                ('send_it', models.BooleanField(default=False)),
                ('User', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]