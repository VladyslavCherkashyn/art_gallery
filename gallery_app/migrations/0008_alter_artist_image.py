# Generated by Django 4.2.2 on 2023-07-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery_app", "0007_artist_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]