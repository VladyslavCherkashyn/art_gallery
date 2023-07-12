# Generated by Django 4.1.7 on 2023-07-12 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fullname", models.CharField(max_length=50, null=True)),
                ("location", models.CharField(max_length=100)),
                ("bio", models.TextField(max_length=100)),
                ("phone", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Artwork",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("image_url", models.URLField()),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("BEIGE", "Beige"),
                            ("BLACK", "Black"),
                            ("BLUE", "Blue"),
                            ("BROWN", "Brown"),
                            ("GOLD", "Gold"),
                            ("GREEN", "Green"),
                            ("GREY", "Grey"),
                            ("ORANGE", "Orange"),
                            ("PINK", "Pink"),
                            ("PURPLE", "Purple"),
                            ("RED", "Red"),
                            ("SILVER", "Silver"),
                            ("WHITE", "White"),
                            ("YELLOW", "Yellow"),
                            ("MULTI", "Multi"),
                            ("BLACK_AND_WHITE", "Black & White"),
                        ],
                        max_length=100,
                    ),
                ),
                ("year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Painting", "Painting"),
                            ("Photography", "Photography"),
                            ("Sculpture", "Sculpture"),
                            ("Prints", "Prints"),
                            ("Work on paper", "Work on paper"),
                            ("Design", "Design"),
                            ("Graphic design", "Graphic design"),
                            ("Collages", "Collages"),
                            ("Illustration", "Illustration"),
                        ],
                        max_length=255,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "artwork",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likess",
                        to="gallery_app.artwork",
                    ),
                ),
            ],
        ),
    ]
