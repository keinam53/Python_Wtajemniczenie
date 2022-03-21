from collections.abc import Generator
from Database_connection import QueryResults, QueryError, DatabaseConnection


def db_connector(connection_str: str) -> Generator[QueryResults, str, None]:
    connection = DatabaseConnection(connection_str)
    try:
        query_result = QueryResults()
        while True:
            query = yield query_result
            query_result = connection.execute(query)
    except QueryError as error:
        print(f'Błąd: {error}')
    finally:
        connection.close()


def run() -> None:
    db = db_connector('postgresql://...')
    next(db)

    select_result = db.send('SELECT...')
    insert_result = db.send('INSERT...')

    print(select_result)
    print(insert_result)
    db.close()


if __name__ == '__main__':
    run()
