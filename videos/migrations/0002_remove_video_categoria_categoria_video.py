# Generated by Django 4.1.6 on 2023-02-13 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="categoria",
        ),
        migrations.AddField(
            model_name="categoria",
            name="video",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="videos.video",
            ),
        ),
    ]
