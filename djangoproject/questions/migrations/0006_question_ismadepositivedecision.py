# Generated by Django 4.2 on 2023-04-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_idk_question_no_question_yes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='isMadePositiveDecision',
            field=models.BooleanField(default=False),
        ),
    ]