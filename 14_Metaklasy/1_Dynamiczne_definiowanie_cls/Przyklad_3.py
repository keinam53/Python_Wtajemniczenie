from typing import Any


# class Bike:
#     def __init__(self, owner: str, model: str) -> None:
#         self.owner = owner
#         self.model = model
#
#     def __str__(self) -> str:
#         return f'Właściciel: {self.owner} , model: {self.model}'


def _bike__init__(self: Any, owner: str, model: str) -> None:
    self.owner = owner
    self.model = model


def _bike__str__(self: Any) -> str:
    return f'Właściciel: {self.owner} , model: {self.model}'


Bike = type("Bike", (), {"__init__": _bike__init__, "__str__": _bike__str__})


def run() -> None:
    rower = Bike('Mariusz', 'kolarka')
    print(rower)


if __name__ == '__main__':
    run()
