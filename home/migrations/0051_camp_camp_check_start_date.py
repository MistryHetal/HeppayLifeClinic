# Generated by Django 4.0.1 on 2022-04-23 12:37

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_delete_camp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(help_text='DD-MM-YYYY', null=True)),
                ('end_date', models.DateTimeField(help_text='DD-MM-YYYY', null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='camp',
            constraint=models.CheckConstraint(check=models.Q(('end_date__gt', django.db.models.expressions.F('start_date'))), name='check_start_date'),
        ),
    ]
