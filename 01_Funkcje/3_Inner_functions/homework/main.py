from new_movies import actions
from new_movies.random_data_utility import random_generator
from new_movies.user import User, Role


def run_example():
    some_movies = random_generator.generate_random_movies(movies_number=15)
    standard_user = User('Mariusz', 'Baran', 5, Role.USER, [])

    actions.rent_movie(standard_user, some_movies[0])
    actions.watch_movie(standard_user, some_movies[0])


if __name__ == "__main__":
    run_example()
