from typing import Any


def _student_init(self: Any, first_name: str, last_name: str) -> None:
    self.first_name = first_name
    self.last_name = last_name


def _student_str(self: Any) -> str:
    return f'Imię: {self.first_name}, Nazwisko: {self.last_name}'


Student = type('Student', (), {'__init__': _student_init, '__str__': _student_str})


def run() -> None:
    student_mariusz = Student('Mariusz', 'Baran')
    print(student_mariusz)


if __name__ == '__main__':
    run()
