from collections import Counter


def run() -> None:
    fruits = Counter({'jabłko': 3, 'banan': 2, 'pomarańcza': 4})
    vegetables: Counter[str] = Counter(pomidor=2, marchewka=4)

    print(fruits)
    print(vegetables)

    print(10 * '-')
    for fruit, quantity in fruits.items():
        print(f'{fruit} -> {quantity}')

    print(10 * '-')
    for fruit in fruits.elements():
        print(fruit)

    print(10 * '-')
    for vegetable, quantity in vegetables.items():
        print(f'{vegetable} -> {quantity}')

    print(10 * '-')
    print(fruits.most_common(1))
    print(fruits.most_common())

    print(10 * '-')
    fruits_order = Counter({'jabłko': 1, 'banan': 1, 'pomarańcza': 10})
    fruits.subtract(fruits_order)
    print(fruits)

    print(10 * '-')
    monday_supply = Counter({'śliwka': 10, 'pomarańcza': 10})
    fruits.update(monday_supply)
    print(fruits)


if __name__ == '__main__':
    run()
