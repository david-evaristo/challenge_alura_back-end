# Generated by Django 4.1.6 on 2023-02-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0002_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="categoriaId",
            field=models.CharField(default=None, max_length=3),
        ),
    ]
