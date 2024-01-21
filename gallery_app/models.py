import os
import uuid
from enum import Enum
from PIL import Image
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


def artworks_thumbnail_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}_thumbnail.{extension}"

    thumbnail_path = os.path.join("artworks", "thumbnails", filename)
    os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
    return thumbnail_path


def resize_image(image_path, output_path, size):
    original_image = Image.open(image_path)
    original_image.thumbnail(size)
    original_image.save(output_path)

# def resize_image(image_path, output_path, size):
#     original_image = Image.open(image_path)
#     original_image.thumbnail(size)
#     output_file_name = f"thumbnail_{os.path.basename(image_path)}"
#     output_file_path = os.path.join("media", "artworks", "thumbnails", output_file_name)
#
#     os.makedirs(output_file_path, exist_ok=True)
#     original_image.save(output_file_path)


def artworks_image_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}.{extension}"
    return os.path.join("artworks/", filename)


def artists_image_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.fullname)}-{uuid.uuid4()}.{extension}"
    return os.path.join("artists/", filename)


class ArtworkColor(Enum):
    BEIGE = "Beige"
    BLACK = "Black"
    BLUE = "Blue"
    BROWN = "Brown"
    GOLD = "Gold"
    GREEN = "Green"
    GREY = "Grey"
    ORANGE = "Orange"
    PINK = "Pink"
    PURPLE = "Purple"
    RED = "Red"
    SILVER = "Silver"
    WHITE = "White"
    YELLOW = "Yellow"
    MULTI = "Multi"
    BLACK_AND_WHITE = "Black & White"

    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]


class ArtworkCategory(Enum):
    PAINTING = "Painting"
    PHOTOGRAPHY = "Photography"
    SCULPTURE = "Sculpture"
    PRINTS = "Prints"
    WORK_ON_PAPER = "Work on paper"
    DESIGN = "Design"
    GRAPHIC_DESIGN = "Graphic design"
    COLLAGES = "Collages"
    ILLUSTRATION = "Illustration"



class Category(models.Model):
    CATEGORY_CHOICES = [(tag.value, tag.value) for tag in ArtworkCategory]

    name = models.CharField(choices=CATEGORY_CHOICES, max_length=255, unique=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    fullname = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100)
    bio = models.TextField(max_length=100)
    categories = models.ManyToManyField(to=Category)
    phone = models.CharField(max_length=50)
    image = models.ImageField(null=True, upload_to=artists_image_path)


class Artwork(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(
        to=Artist, on_delete=models.CASCADE, related_name="artworks"
    )
    image_url = models.ImageField(null=True, upload_to=artworks_image_path)
    image_thumbnail = models.ImageField(null=True, upload_to=artworks_thumbnail_path)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    likes = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="liked_artworks", through="Like")
    categories = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="artworks"
    )

    COLOR_CHOICES = [(tag.name, tag.value) for tag in ArtworkColor]

    color = models.CharField(choices=COLOR_CHOICES, max_length=100)
    year = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image_url and not self.image_thumbnail:
            # thumbnail_path = artworks_thumbnail_path(self, self.image_url)
            resize_image(self.image_url, self.image_thumbnail, (100, 100))

            self.save(update_fields=['image_thumbnail'])


@receiver(post_save, sender=Artwork)
def create_thumbnail(sender, instance, **kwargs):
    if instance.image_url and not instance.image_thumbnail:
        thumbnail_path = artworks_thumbnail_path(instance, instance.image_url.name)
        resize_image(instance.image_url.path, thumbnail_path, (100, 100))
        instance.image_thumbnail.name = thumbnail_path[len('artworks/thumbnails/'):]
        instance.save(update_fields=['image_thumbnail'])

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='likess')

    class Meta:
        unique_together = ("user", "artwork")
