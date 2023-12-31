# Generated by Django 4.2.6 on 2023-10-21 17:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("transcriber", "0003_rename_files_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="file_id",
            field=models.UUIDField(default=uuid.UUID("c6d713f1-4781-4e29-9ed5-acf6bbc83b0d")),
        ),
        migrations.AddField(
            model_name="file",
            name="is_transcribed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="file",
            name="transcribed_text",
            field=models.TextField(null=True),
        ),
    ]
