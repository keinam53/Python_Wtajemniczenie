from typing import Protocol, Type, TypeVar, Any


class Named(Protocol):
    first_name: str
    last_name: str


T = TypeVar("T", bound=Type[Named])


def str_for_name(self: Named) -> str:
    return f'{self.first_name} {self.last_name}'


class NameBasedStrMeta(type):
    def __new__(mcs, name: str, bases: tuple[type], class_dict: dict[str, None]) -> Any:
        class_dict['__str__'] = str_for_name
        return super().__new__(mcs, name, bases, class_dict)


class Student(metaclass=NameBasedStrMeta):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self) -> None:
        print(f"Cześć, mam na inię {self.first_name}")


def run_example() -> None:
    student_mariusz = Student("Mariusz", "Baran")
    print(student_mariusz)


if __name__ == "__main__":
    run_example()
