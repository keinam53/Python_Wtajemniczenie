from datetime import datetime
from zoneinfo import ZoneInfo


def run():
    czas_utc = datetime(year=2021, month=4, day=5, hour=3, minute=20, tzinfo=ZoneInfo("UTC"))
    czas_wwa = datetime(
        year=2021, month=4, day=5, hour=5, minute=20, tzinfo=ZoneInfo("Europe/Warsaw")
    )
    czas_ny_1 = datetime(
        year=2021, month=4, day=4, hour=20, minute=50, tzinfo=ZoneInfo("America/New_York")
    )
    czas_ny_2 = datetime(
        year=2021, month=4, day=4, hour=23, minute=50, tzinfo=ZoneInfo("America/New_York")
    )

    print(czas_utc)
    print(czas_wwa)
    print(czas_ny_1)
    print(czas_ny_2)

    print("czas_utc < czas_wwa", czas_utc < czas_wwa)
    print("czas_utc == czas_wwa", czas_utc == czas_wwa)
    print("czas_ny_1 > czas_wwa", czas_ny_1 > czas_wwa)
    print("czas_ny_2 > poland_time", czas_ny_2 > czas_wwa)


if __name__ == "__main__":
    run()
