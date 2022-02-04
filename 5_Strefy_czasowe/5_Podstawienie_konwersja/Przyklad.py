from datetime import datetime
from zoneinfo import ZoneInfo


def run():
    utc_4 = datetime.fromisoformat('2022-02-02 15:33:59+04:00')
    print(utc_4.replace(tzinfo=ZoneInfo('Europe/Warsaw')))

    naiwna_date = datetime.fromisoformat('2022-02-02 15:33:59')
    print(naiwna_date.replace(tzinfo=ZoneInfo('America/New_York')))

    czas_utc_4 = utc_4.timetz()
    print(czas_utc_4.replace(tzinfo=ZoneInfo('UTC')))


if __name__ == '__main__':
    run()
