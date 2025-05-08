import strawberry

@strawberry.input
class MovieInput:
  title: str
  release_date: str # formato: "YYYY-MM-DD"
  director: str
  genre_ids: list[int]

@strawberry.input
class ReviewInput:
    reviewer_name: str
    rating: int
    comment: str
    movie_id: int

@strawberry.input
class GenreInput:
    name: str