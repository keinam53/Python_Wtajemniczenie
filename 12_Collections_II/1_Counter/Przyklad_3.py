from collections import Counter


def run() -> None:
    my_fruits = Counter({'jabłko': 5, 'banan': 2, 'pomarańcza': 4})
    your_fruits = Counter({'jabłko': 3, 'śliwka': 10, 'ananas': 3})

    print(my_fruits)
    print(your_fruits)
    print(10 * '-')

    print(my_fruits + your_fruits)
    print(10 * '-')

    print(my_fruits - your_fruits)
    print(10 * '-')
    # min(my_fruits[...], your_fruits[...])
    print(my_fruits & your_fruits)
    print(10 * '-')
    # max(my_fruits[...], your_fruits[...])
    print(my_fruits | your_fruits)
    print(10 * '-')

    my_fruits.subtract({'jabłko': 10})
    print(my_fruits)
    print(+my_fruits)
    print(-my_fruits)


if __name__ == '__main__':
    run()
