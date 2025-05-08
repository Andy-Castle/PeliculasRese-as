import strawberry
import strawberry_django
from strawberry import auto
from .models import Movie, Genre, Review

@strawberry_django.type(Movie)
class MovieType:
  id: auto
  title: auto
  release_date: auto
  director: auto
  gender: list["GenreType"]

@strawberry_django.type(Genre)
class GenreType:
  id: auto
  name: auto
  movie_set: list[MovieType]

@strawberry_django.type(Review)
class ReviewType:
  id: auto
  reviewer_name: auto
  rating: auto
  comment: auto
  movies = MovieType