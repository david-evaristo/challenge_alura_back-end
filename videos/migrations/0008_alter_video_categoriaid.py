# Generated by Django 4.1.6 on 2023-02-11 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0007_alter_video_categoriaid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="categoriaId",
            field=models.IntegerField(),
        ),
    ]