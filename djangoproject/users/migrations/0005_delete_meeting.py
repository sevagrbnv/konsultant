# Generated by Django 4.1.7 on 2023-04-04 11:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_meeting"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Meeting",
        ),
    ]
