from datetime import date

from example_system import datetime_calculations


def run_example() -> None:
    print(datetime_calculations.is_easter(date(year=2022, month=4, day=17)))
    print(datetime_calculations.is_easter(date(year=2021, month=4, day=17)))


if __name__ == "__main__":
    run_example()
