# Generated by Django 4.2 on 2023-04-15 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meetings', '0012_meeting_protocol_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='meetings.meeting')),
            ],
        ),
    ]
