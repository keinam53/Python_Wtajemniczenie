from datetime import datetime
from zoneinfo import ZoneInfo


def run():
    wwa_czas_letni = datetime(2020, 10, 20, tzinfo=ZoneInfo('Europe/Warsaw'))
    wwa_czas_zimowy = datetime(2020, 10, 30, tzinfo=ZoneInfo('Europe/Warsaw'))

    print(wwa_czas_letni)
    print(wwa_czas_zimowy)

    przed_zmiana_czasu = datetime(2020, 10, 25, 2, 30, tzinfo=ZoneInfo('Europe/Warsaw'), fold=0)
    po_zmianie_czasu = datetime(2020, 10, 25, 2, 30, tzinfo=ZoneInfo('Europe/Warsaw'), fold=1)

    print(przed_zmiana_czasu)
    print(po_zmianie_czasu)


if __name__ == '__main__':
    run()
