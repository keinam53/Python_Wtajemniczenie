from __future__ import annotations


class Student:
    def __new__(cls, *args: str, **kwargs: str) -> Student:
        return super().__new__(cls)

    def __init__(self, frst_name: str, last_name: str) -> None:
        self.frst_name = frst_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.frst_name} {self.last_name}"


def run() -> None:
    student_mariusz = Student('Mariusz', 'Baran')
    print(student_mariusz)


if __name__ == '__main__':
    run()
