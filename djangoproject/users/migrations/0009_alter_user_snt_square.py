# Generated by Django 4.2 on 2023-04-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_snt_doc_id_user_snt_square'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_snt',
            name='square',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
