from datetime import timedelta, date


def run():
    luty_28_2020 = date(year=2020, month=2, day=28)
    luty_28_2021 = date(year=2021, month=2, day=28)
    one_day = timedelta(days=1)

    print(luty_28_2020 + one_day)
    print(luty_28_2021 + one_day)


if __name__ == '__main__':
    run()
