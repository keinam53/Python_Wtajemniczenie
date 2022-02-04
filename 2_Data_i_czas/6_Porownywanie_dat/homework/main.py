from new_movies import actions
from new_movies.movies_directory import available_movies
from new_movies.user import User, Role


def run_example():
    user = User('Mariusz', 'Baran', 3, Role.USER, [])

    actions.rent_movie(user, available_movies[1])
    actions.watch_movie(user, available_movies[1])
    actions.watch_movie(user, available_movies[1])
    actions.watch_movie(user, available_movies[1])
    actions.watch_movie(user, available_movies[1])
    actions.watch_movie(user, available_movies[1])


if __name__ == "__main__":
    run_example()
