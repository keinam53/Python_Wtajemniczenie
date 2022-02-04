from datetime import date
from new_movies.user import User, Role
from new_movies.exceptions import UserNotFound


available_users = [
    User(
        first_name='Mariusz',
        last_name='Baran',
        login='Mariusz',
        # birth_date=date(year=194, month=8, day=27),
        birth_date=date(year=2015, month=1, day=1),
        credits_left=5,
        role=Role.USER,
        rented_movies=[],
    )]


def find_user_by_login(login):
    lower_case_login = login.lower()
    for user in available_users:
        if lower_case_login == user.login.lower():
            return user
        raise UserNotFound()
