from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')


def run() -> None:
    lista_liter = ['A', 'B', 'C', 'D', 'E', 'F']
    lista_cyfr = [1, 2, 3, 4, 5, 6, 7]
    ostatnia_litera = ostatni_element(lista_liter)
    ostatnia_cyfra = ostatni_element(lista_cyfr)
    reveal_type(ostatnia_litera)
    reveal_type(ostatnia_cyfra)


def ostatni_element(sequence: Sequence[T]) -> T:
    return sequence[-1]
