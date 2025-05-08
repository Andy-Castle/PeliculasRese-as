import strawberry
import strawberry_django
from typing import List
from .types import MovieType, ReviewType, GenreType
from .models import Movie, Review, Genre
from .inputs import MovieInput, ReviewInput, GenreInput, MovieUpdate, ReviewUpdate, GenreUpdate
from dataclasses import asdict
from django.db import connection

@strawberry.type
class Query:
    # Consulta para listar todas las películas
    all_movies: List[MovieType] = strawberry_django.field()

    # Consulta SQL personalizada para películas con calificación baja
    @strawberry.field
    def poorly_rated_movies(self) -> List[str]:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT DISTINCT m.title
                FROM cinema_movie m
                JOIN cinema_review r ON r.movies_id = m.id
                WHERE r.rating < 2
            """)
            rows = cursor.fetchall()
            return [row[0] for row in rows]
        

#Los crud
@strawberry.type
class Mutations:
    @strawberry.mutation
    def create_genre(self, input: GenreInput) -> GenreType:
        genre = Genre.objects.create(name=input.name)
        return genre
    
    @strawberry.mutation
    def create_movie(self, input: MovieInput) -> MovieType:
        movie = Movie.objects.create(
            title=input.title,
            release_date=input.release_date,
            director=input.director,
        )
        if input.genre_ids:
            movie.gender.set(input.genre_ids)
        return movie
    
    @strawberry.mutation
    def create_review(self, input: ReviewInput) -> ReviewType:
        review = Review.objects.create(
            reviewer_name=input.reviewer_name,
            rating=input.rating,
            comment=input.comment,
            movies_id=input.movie_id
        )
        return review
    
    
    @strawberry.mutation
    def update_movie(self, movie_id: int, data: MovieUpdate) -> MovieType:
        try:
            movie = Movie.objects.get(id=movie_id)
            for key, value in asdict(data).items():
                setattr(movie, key, value)
            
            movie.save()
        except Movie.DoesNotExist:
            raise Exception("Not found")