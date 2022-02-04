from new_movies.datetime_preferences import DatetimePreference
from new_movies.exceptions import ActionNotAllowed, UserNotFound
from new_movies.auth_context import AuthContext
from new_movies import permissions, users_directory


def login():
    auth_context = AuthContext()
    while True:
        user_login = input('Podaj login: ')
        auth_context.register_login_attempt()
        if auth_context.should_reject_attempt_due_to_lock_time():
            auth_context.register_failed_login_attempt()
            print('Próba jest ignorowana z powodu przekroczenia rozszeżonej ilości prób logowania')
            print(f'Proszę poczekać {auth_context.lock_time} przed kolejną próbą')
            continue
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            auth_context.register_failed_login_attempt()
            print('Nie znaleziono użytkownika o podanym loginie -spróbuj ponownie')
            if auth_context.is_failures_limit_exceeded():
                print(f"Został przekroczony limit prób logowania. Proszę poczekać {auth_context.lock_time}")


def select_datetime_preferences(user):
    print('Dostępne formaty daty i czasu:')
    for option_index, datetime_preferences in enumerate(DatetimePreference):
        print(f'{option_index} {datetime_preferences}')

    selected_option = int(input("Wybierz opcje: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()
