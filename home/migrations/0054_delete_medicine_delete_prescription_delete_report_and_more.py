# Generated by Django 4.0.1 on 2022-04-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_alter_camp_camp_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='medicine',
        ),
        migrations.DeleteModel(
            name='prescription',
        ),
        migrations.DeleteModel(
            name='report',
        ),
        migrations.DeleteModel(
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='user',
        ),
        migrations.DeleteModel(
            name='treatement',
        ),
        migrations.AlterModelOptions(
            name='mail',
            options={'verbose_name': 'Prescription User', 'verbose_name_plural': 'Precription Users'},
        ),
        migrations.AlterModelOptions(
            name='mailtext',
            options={'verbose_name': 'Prescription to send', 'verbose_name_plural': 'Prescription to send'},
        ),
        migrations.AlterField(
            model_name='mailtext',
            name='attachment',
            field=models.CharField(help_text='Type Patient prescription..', max_length=250),
        ),
        migrations.AlterField(
            model_name='mailtext',
            name='message',
            field=models.CharField(help_text='Type Patient Email..', max_length=50),
        ),
        migrations.AlterField(
            model_name='mailtext',
            name='subject',
            field=models.CharField(help_text='Type Patient Email..', max_length=50),
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
