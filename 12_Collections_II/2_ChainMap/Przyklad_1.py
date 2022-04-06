from collections import ChainMap


def run() -> None:
    class_a_grades = {"Jan": 4, "Mariusz": 5, "Mikołaj": 3, "Joanna": 4}
    class_b_grades = {"Jacek": 4, "Witold": 5, "Anna": 3, "Bożena": 4}
    results = ChainMap(class_a_grades, class_b_grades)
    for student, grade in results.items():
        print(f'{student} - {grade}')
    print(10 * '-')

    class_b_grades['Anna'] = 5
    for student, grade in results.items():
        print(f'{student} - {grade}')


if __name__ == '__main__':
    run()
