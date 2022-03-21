from datetime import timedelta


def run():
    interwal = timedelta(days=1, seconds=1, microseconds=1, milliseconds=1, minutes=1, hours=1, weeks=1)

    print(interwal)
    print(interwal.days)
    print(interwal.seconds)
    print(interwal.microseconds)

    interwal_dodatni = timedelta(seconds=10)
    interwal_ujemny = timedelta(seconds=-10)
    print(f'Interwał dodatni: {interwal_dodatni}')
    print(f'Interwał ujemny: {interwal_ujemny}')

    print(f'Interwał dodatni: {interwal_dodatni.total_seconds()}')
    print(f'Interwał ujemny: {interwal_ujemny.total_seconds()}')


if __name__ == '__main__':
    run()
