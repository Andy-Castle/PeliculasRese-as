from django.db import models

# Create your models here.
class Genre(models.Model):
  name = models.CharField(max_length=100)

class Movie(models.Model):
  title = models.CharField(max_length=100)
  release_date = models.DateField()
  director = models.CharField(max_length=100)
  gender = models.ManyToManyField(Genre) # Muchos a muchos de Genre - Movie

class Review(models.Model):
  reviewer_name = models.CharField(max_length=100)
  rating = models.IntegerField()
  comment = models.TextField(max_length=1000)
  movies = models.ForeignKey(Movie, on_delete=models.CASCADE) #Uno a muchos Movie - Review

