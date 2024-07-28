from django.db import models


class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def __str__(self):
        return self.album_name


class Song(models.Model):
    song_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
    )

    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
        related_name='songs',
    )
