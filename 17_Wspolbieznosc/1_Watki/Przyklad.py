import time
import threading


def czas() -> None:
    time.sleep(2)


def wypisz() -> None:
    print(f'Nowy wątek - ID: {threading.get_ident()}')
    czas()


def run() -> None:
    for i in range(10):
        threading.Thread(target=wypisz).start()


if __name__ == '__main__':
    run()
