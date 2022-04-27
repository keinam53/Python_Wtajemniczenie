from typing import Any


class SimpleMetaclass(type):
    def __new__(mcs, name: str, bases: tuple[type], class_dict: dict[str, Any]) -> Any:
        print(f'Zdefiniowana klasa: {name}')
        print(f'Klasy bazowe: {bases}')
        print(f'Wnętrze klasy: {class_dict}')
        return super().__new__(mcs, name, bases, class_dict)


class Human(metaclass=SimpleMetaclass):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'Imię: {self.first_name}, Nazwisko: {self.last_name}'


class Movie(metaclass=SimpleMetaclass):
    def __init__(self, name: str, category: str) -> None:
        self.name = name
        self.category = category

    def __str__(self) -> str:
        return f'Nazwa: {self.name}, Kategorti: {self.category}'


def run():
    mariusz = Human('Mariusz', 'Baran')
    hobbit = Movie('Hobbit', 'Fantasy')
    print(mariusz)
    print(hobbit)


if __name__ == '__main__':
    run()
