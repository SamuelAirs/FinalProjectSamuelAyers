# Generated by Django 5.0.4 on 2024-04-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminderbase',
            name='reminderDetails',
        ),
        migrations.AddField(
            model_name='reminderdetails',
            name='reminderDetails',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
