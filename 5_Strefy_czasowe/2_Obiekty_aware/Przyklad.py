from datetime import datetime
from zoneinfo import ZoneInfo


def run():
    data_czas_today = datetime.today()
    data_czas_now = datetime.now()
    now_wwa = datetime.now(tz=ZoneInfo('Europe/Warsaw'))
    now_ny = datetime.now(tz=ZoneInfo('America/New_York'))

    print(data_czas_today)
    print(data_czas_now)
    print(now_wwa)
    print(now_ny)

    print(now_wwa == now_ny)
    print(now_wwa.replace(microsecond=0) == now_ny.replace(microsecond=0))

    
if __name__ == '__main__':
    run()
