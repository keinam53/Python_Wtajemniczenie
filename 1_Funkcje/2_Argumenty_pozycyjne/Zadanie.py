def my_formatter(string, /, **values):
    for formatting_name, value in values.items():
        search_pattern = f"<{formatting_name}>"
        string = string.replace(search_pattern, value)
    return string


def run_example():
    result = my_formatter("<greeting>, my name is <name>", greeting="Hello", name="Mariusz")
    print(result)

    result = my_formatter("Just output this: <string>", string="Some text")
    print(result)


if __name__ == '__main__':
    run_example()
