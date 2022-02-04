from datetime import datetime


def run():
    data_czas = datetime.fromordinal(738_000)
    print(data_czas)
    print(data_czas.toordinal())
    print(data_czas.weekday())
    print(data_czas.isoweekday())

    data_czas_inny = datetime.fromtimestamp(1_600_000_000)
    print(data_czas_inny)
    print(data_czas_inny.timestamp())
    print(data_czas_inny.isocalendar())


if __name__ == '__main__':
    run()
