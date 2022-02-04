from datetime import date

from new_movies import permissions, movies_directory, cinema_schedule
from new_movies.exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached,
)
from new_movies.movie import Movie
from new_movies.rented_movie import RentedMovie
from new_movies.cinema_schedule import Weekday
from new_movies.configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1


def watch_movie(user, movie):
    rented_movie = _get_rented_movie(user, movie)
    if not rented_movie:
        raise MovieNotFound()

    if _unlimited_watching_promo():
        _watch_movie_during_unlimited_promo(user, rented_movie)
    else:
        _watch_movie_during_standard_period(user, rented_movie)


def _unlimited_watching_promo():
    return UNLIMITED_WATCHING_START_DATE <= date.today() <= UNLIMITED_WATCHING_END_DATE


def _watch_movie_during_unlimited_promo(user, rented_movie):
    _start_streaming(user, rented_movie.movie)


def _watch_movie_during_standard_period(user, rented_movie):
    if rented_movie.views_left < 1:
        raise ViewsLimitReached()

    rented_movie.views_left -= 1
    _start_streaming(user, rented_movie.movie)


def _get_rented_movie(user, movie):
    for rented_movie in user.rented_movies:
        if rented_movie.movie == movie:
            return rented_movie


def _start_streaming(user, movie):
    print(f"User: {user} is watching {movie}")


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()


def add_movie():
    print("Dodawanie nowego filmu")
    print("Wprowadź podstawowe informacje o filmie")
    name = input("Tytuł: ")
    category = input("Kategoria: ")
    release_date_input = input('Data wydania w formacie RRRR-MM-DD: ')
    release_date = date.fromisoformat(release_date_input)
    new_movie = Movie(name=name, category=category, release_date=release_date)
    movies_directory.add_movie(new_movie)


def cinema_movies_schedule():
    cinema_date_input = input('Kiedy chcesz iść do kina? (YYYY-MM-DD): ')
    cinema_date = date.fromisoformat(cinema_date_input)
    weekday_number = date.isoweekday(cinema_date)
    weekday = Weekday(weekday_number)
    print('Tego dnia możesz obejrzeć: ')
    for movie_showtime in cinema_schedule.get_movies_showtime_by_weekday(weekday):
        print(f'{movie_showtime.showtime} {movie_showtime.movie}')
