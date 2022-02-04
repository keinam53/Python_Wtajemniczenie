def words_connector(connect_char):
    def connect(text):
        return text.replace(" ", connect_char)
    return connect


def run():
    minus_connector = words_connector("-")
    plus_connector = words_connector("+")
    pipe_connector = words_connector("|")

    text = 'Dzisiejsza pogoda jest piękna'
    print(text)
    print(minus_connector(text))
    print(plus_connector(text))
    print(pipe_connector(text))


if __name__ == '__main__':
    run()
