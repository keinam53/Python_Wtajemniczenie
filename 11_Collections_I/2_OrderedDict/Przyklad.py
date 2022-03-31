from collections import OrderedDict


def run() -> None:
    elements: OrderedDict[str, int] = OrderedDict({'jabłko': 3, 'banan': 5, 'pomarańcza': 1})

    for element, quantity in elements.items():
        print(element, quantity)
    print(10 * '-')

    for element, quantity in reversed(elements.items()):
        print(element, quantity)
    print(10 * '-')

    elements.move_to_end('jabłko')
    for element, quantity in elements.items():
        print(element, quantity)
    print(10 * '-')

    print(elements.popitem(last=False))
    print(elements)


if __name__ == '__main__':
    run()
