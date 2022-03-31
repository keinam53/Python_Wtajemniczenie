from movie import Movie
from movie_service import MovieServiceConnection


def load_available_movies() -> list[Movie]:
    with MovieServiceConnection() as movies_service:
        movies: list[Movie] = []
        for _ in range(4):
            movie_name = movies_service.get_movie()
            movies.append(Movie(movie_name))
        return movies