from new_movies.cinema_schedule import (
    generate_january_week_schedule,
    weekly_schedule,
    Weekday,
    sort_weekly_schedule,
)


def run_example():
    sorted_weekly_schedule = sort_weekly_schedule(weekly_schedule)
    january_week_schedule = generate_january_week_schedule(sorted_weekly_schedule)
    print('Podczas ostatniego tygodnia stycznia możesz obejrzeć: ')
    for week_day in Weekday:
        print(f'W {week_day.name}: ')
        for movie_showtime in january_week_schedule[week_day]:
            print(movie_showtime.showdatetime, movie_showtime.movie)


if __name__ == "__main__":
    run_example()
