from datetime import datetime
from zoneinfo import ZoneInfo


def run():
    utc_4 = datetime.fromisoformat('2022-02-02 15:33:59+04:00')
    print(utc_4)
    print(utc_4.replace(tzinfo=ZoneInfo('Europe/Warsaw')))
    print(utc_4.astimezone(tz=ZoneInfo('America/New_York')))

    naiwny_datetime = datetime.fromisoformat('2022-02-02 19:33:59')
    print(naiwny_datetime.astimezone(tz=ZoneInfo('America/New_York')))

    print(utc_4.astimezone())


if __name__ == '__main__':
    run()
