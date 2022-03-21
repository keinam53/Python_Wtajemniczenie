from datetime import datetime
from zoneinfo import ZoneInfo


def run():
    utc_naiwny = datetime.utcnow()
    utc_swiadomy = datetime.now(tz=ZoneInfo('UTC'))

    print(utc_naiwny)
    print(utc_swiadomy)

    print(utc_naiwny.astimezone(tz=ZoneInfo('Europe/Warsaw')))
    print(utc_swiadomy.astimezone(tz=ZoneInfo('Europe/Warsaw')))


if __name__ == '__main__':
    run()
