from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Ocena:
    wartosc: int
    OCENA_NEGATYWNA: ClassVar = 1

    def zaliczenie(self):
        return self.wartosc > Ocena.OCENA_NEGATYWNA


def run():
    ocena = None
    ocena = Ocena(wartosc=3)
    ocena.zaliczenie()
    print('Zaliczone')
    ocena = 3
    print('Ocena 3')
    # ocena.is_passing() Błąd 'int' object has no attribute 'is_passing'


if __name__ == '__main__':
    run()
