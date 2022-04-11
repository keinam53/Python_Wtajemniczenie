from typing import TypeVar, Type, Protocol


class Named(Protocol):
    first_name: str
    last_name: str


T = TypeVar('T', bound=Type[Named])


def name_based_str(cls: T) -> T:
    def str_from_name(self: Named) -> str:
        return f'{self.first_name} {self.last_name}'

    cls.__str__ = str_from_name
    return cls


@name_based_str
class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self) -> None:
        print(f'Cześć, mam na imię {self.first_name}')


def run() -> None:
    student_mariusz = Student('Mariusz', 'Baran')
    print(student_mariusz)


if __name__ == '__main__':
    run()
