# Generated by Django 4.2 on 2023-04-13 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0007_alter_meeting_date_alter_meeting_notification_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='notification_date',
            new_name='form',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='time',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='time2',
        ),
    ]