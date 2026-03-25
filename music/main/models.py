from django.db import models

class Genre(models.Model):
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    def __str__ (self):
        return self.name_en


class Track(models.Model):
    name = models.CharField(max_length=500)
    duretion = models.FloatField()
    genre = models.ManyToManyField(Genre)
    def __str__ (self):
        return self.name

class genre_track(models.Model):
   genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
   track = models.ForeignKey(Track, on_delete=models.CASCADE)
  
