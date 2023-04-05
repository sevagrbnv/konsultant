# Generated by Django 4.1.7 on 2023-04-05 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("meetings", "0003_alter_meeting_snt_id"),
        ("docs", "0002_alter_doc_meeting_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doc",
            name="meeting_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="docs",
                to="meetings.meeting",
            ),
        ),
    ]