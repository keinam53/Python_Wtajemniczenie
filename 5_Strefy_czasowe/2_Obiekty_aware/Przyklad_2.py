from datetime import datetime
from zoneinfo import ZoneInfo


def run():
    timestamp = 1611075878
    data_czas = datetime.fromtimestamp(timestamp)
    data_czas_wwa = datetime.fromtimestamp(timestamp, tz=ZoneInfo('Europe/Warsaw'))
    data_czas_ny = datetime.fromtimestamp(timestamp, tz=ZoneInfo('America/New_York'))

    print(data_czas)
    print(data_czas_wwa)
    print(data_czas_ny)

    print(data_czas_wwa == data_czas_ny)
    print(data_czas_wwa == data_czas)
    # print(data_czas_wwa > data_czas) BŁĄD


if __name__ == '__main__':
    run()
