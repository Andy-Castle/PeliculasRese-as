import strawberry
import strawberry_django
from .models import Movie, Genre, Review

#Crete
@strawberry_django.input(Movie)
class MovieInput:
  title: str
  release_date: str # formato: "YYYY-MM-DD"
  director: str
  genre_ids: list[int]

@strawberry_django.input(Review)
class ReviewInput:
    reviewer_name: str
    rating: int
    comment: str
    movie_id: int

@strawberry_django.input(Genre)
class GenreInput:
    name: str


#Update
@strawberry_django.input(Movie)
class MovieUpdate:
  title: str | None = None
  release_date: str | None = None
  director: str | None = None
  genre_ids: list[int] | None = None

@strawberry_django.input(Review)
class ReviewUpdate:
    reviewer_name: str | None = None
    rating: int | None = None
    comment: str | None = None
    movie_id: int | None = None

@strawberry_django.input(Genre)
class GenreUpdate:
    name: str | None = None