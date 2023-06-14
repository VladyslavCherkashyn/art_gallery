# # Generated by Django 4.2.2 on 2023-06-12 13:17
#
# from django.db import migrations, models
# import django.db.models.deletion
#
#
# class Migration(migrations.Migration):
#     dependencies = [
#         ('gallery_app', '0001_initial'),
#     ]
#
#     operations = [
#         migrations.CreateModel(
#             name='Artist',
#             fields=[
#                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('fullname', models.CharField(max_length=50, null=True)),
#                 ('location', models.CharField(max_length=100)),
#                 ('bio', models.TextField(max_length=100)),
#                 ('phone', models.CharField(max_length=50)),
#                 ('mediums', models.ManyToManyField(to='gallery_app.Medium')),
#             ],
#         ),
#         migrations.AlterField(
#             model_name='artwork',
#             name='artist',
#             field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='gallery_app.Artist'),
#         ),
#     ]
# Generated by Django 4.2.2 on 2023-06-12 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("gallery_app", "0002_initial"),
    ]

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
                ("mediums", models.ManyToManyField(to="gallery_app.medium")),
            ],
        ),
        migrations.AlterField(
            model_name="artwork",
            name="artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="artworks",
                to="gallery_app.artist",
            ),
        ),
    ]