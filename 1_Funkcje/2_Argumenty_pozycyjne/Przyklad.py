def example_func(pos_1, /, pos_or_key, *, key):
    print(pos_1, pos_or_key, key)


def run_example():
    example_func(5, 10, key=15)
    example_func(5, pos_or_key=10, key=15)


if __name__ == '__main__':
    run_example()
