# Generated by Django 4.2 on 2023-04-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0011_meeting_place_meeting_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='protocol_date',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
