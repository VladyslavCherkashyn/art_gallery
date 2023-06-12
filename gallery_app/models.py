from django.db import models


class Artwork(models.Model):
    title = models.CharField(max_length=255)
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artworks")
    image_url = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    likes = models.ManyToManyField("auth.User", related_name="liked_artworks", blank=True)
    style = models.ForeignKey("Style", on_delete=models.CASCADE, related_name="artworks")
    medium = models.ManyToManyField("Medium", on_delete=models.CASCADE, related_name="artworks")

    def __str__(self):
        return self.title


class Style(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Medium(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
