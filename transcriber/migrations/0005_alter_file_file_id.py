# Generated by Django 4.2.6 on 2023-10-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transcriber", "0004_file_file_id_file_is_transcribed_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file_id",
            field=models.UUIDField(),
        ),
    ]