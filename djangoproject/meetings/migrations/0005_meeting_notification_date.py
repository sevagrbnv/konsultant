# Generated by Django 4.2 on 2023-04-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_meeting_is_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='notification_date',
            field=models.CharField(default='01.01.23', max_length=10),
            preserve_default=False,
        ),
    ]
