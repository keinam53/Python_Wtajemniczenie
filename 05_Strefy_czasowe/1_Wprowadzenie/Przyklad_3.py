from datetime import time, datetime
from zoneinfo import ZoneInfo


def run():
    czas_naiwny = time(18, 20, 30)
    czas_swiadomy_wwa = time(18, 20, 30, tzinfo=ZoneInfo('Europe/Warsaw'))
    czas_swiadomy_utc = time(18, 20, 30, tzinfo=ZoneInfo('UTC'))

    print(czas_naiwny, czas_naiwny.tzinfo)
    print(czas_swiadomy_wwa, czas_swiadomy_wwa.tzinfo)
    print(czas_swiadomy_utc, czas_swiadomy_utc.tzinfo)

    # czas_swiadomy_wwa = time(18, 20, 30, tzinfo=ZoneInfo('Etc/GMT-2'))
    # print(czas_swiadomy_wwa, czas_swiadomy_wwa.tzinfo)

    przed_zmiana_czasu = time(2, 30, tzinfo=ZoneInfo('Europe/Warsaw'), fold=0)
    po_zmianie_czasu = time(2, 30, tzinfo=ZoneInfo('Europe/Warsaw'), fold=1)
    print(przed_zmiana_czasu, przed_zmiana_czasu.tzinfo)
    print(po_zmianie_czasu, po_zmianie_czasu.tzinfo)

    przed_zmiana_czasu = time(2, 30, tzinfo=ZoneInfo('Etc/GMT-2'), fold=0)
    po_zmianie_czasu = time(2, 30, tzinfo=ZoneInfo('Etc/GMT-1'), fold=1)
    print(przed_zmiana_czasu, przed_zmiana_czasu.tzinfo)
    print(po_zmianie_czasu, po_zmianie_czasu.tzinfo)

    data_czas_wwa = datetime(2020, 10, 30, tzinfo=ZoneInfo('Europe/Warsaw'))

    print(czas_swiadomy_utc.tzinfo.utcoffset(None))
    print(czas_swiadomy_wwa.tzinfo.utcoffset(None))
    print(data_czas_wwa.tzinfo.utcoffset(data_czas_wwa))


if __name__ == '__main__':
    run()
