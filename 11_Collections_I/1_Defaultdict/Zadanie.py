from collections import defaultdict


def load_movies() -> dict[str, list[str]]:
    movies: dict[str, list[str]] = defaultdict(list)
    with open('movies.txt') as movies_file:
        for line in movies_file:
            movie_data = line.split(' - ')
            movie_name = movie_data[0]
            movie_category = movie_data[1]
            movies[movie_category].append(movie_name)
    return movies


def run() -> None:
    category_name = load_movies()
    for categories, names in category_name.items():
        print(f'{categories}', end='')
        for name in names:
            print(f' - {name}')


if __name__ == '__main__':
    run()

