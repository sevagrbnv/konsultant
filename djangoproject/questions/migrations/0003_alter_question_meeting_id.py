# Generated by Django 4.1.7 on 2023-04-04 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("meetings", "0003_alter_meeting_snt_id"),
        ("questions", "0002_alter_question_idk_alter_question_no_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="meeting_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="meetings.meeting",
            ),
        ),
    ]