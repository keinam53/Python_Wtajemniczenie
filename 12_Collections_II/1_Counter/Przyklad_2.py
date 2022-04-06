from collections import Counter


def run() -> None:
    fruits = Counter({'jabłko': 3, 'banan': 2, 'pomarańcza': 4})
    print(fruits['śliwka'])
    fruits['śliwka'] += 1
    print(fruits)

    print(10 * '-')
    del fruits['jabłko']
    for fruit, quantity in fruits.items():
        print(f'{fruit} -> {quantity}')
        

if __name__ == '__main__':
    run()
