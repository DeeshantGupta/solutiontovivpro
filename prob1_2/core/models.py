from django.db import models

# Create your models here.

class Song(models.Model):
    index = models.IntegerField(auto_created=True, primary_key=True)
    id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.IntegerField()
    loudness = models.FloatField()
    mode = models.IntegerField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    duration_ms = models.IntegerField()
    time_signature = models.IntegerField()
    num_bars = models.IntegerField()
    num_sections = models.IntegerField()
    num_segments = models.IntegerField()
    Class = models.IntegerField()
    star_rating = models.FloatField(default=0)

    def __str__(self):
        return self.title