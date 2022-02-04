from datetime import datetime, date, time
from zoneinfo import ZoneInfo


def run():
    naiwna_data = date.fromisoformat('2022-02-02')
    naiwny_czas = time.fromisoformat('15:03:39')
    swiadomy_czas = time.fromisoformat('15:03:39+01:00')

    #naiwny datetime
    print(datetime.combine(naiwna_data, naiwny_czas))

    #śeiadomy datetime
    print(datetime.combine(naiwna_data, naiwny_czas, tzinfo=ZoneInfo('America/New_York')))

    #świadomy datetime
    print(datetime.combine(naiwna_data, swiadomy_czas))


if __name__ == '__main__':
    run()
