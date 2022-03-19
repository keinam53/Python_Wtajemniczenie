class QueryResults:
    pass


class QueryError(Exception):
    pass


class DatabaseConnection:
    def __init__(self, connection_str: str) -> None:
        self.connection_str = connection_str
        self.connection_handler = None

    def execute(self, query: str) -> QueryResults:
        print(f'Wykonanie: {query}')
        return QueryResults()

    def close(self) -> None:
        print('Zamknięcie połączenia')
