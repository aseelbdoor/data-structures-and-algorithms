from python.sorting.Comparisons.sort import Movie,sort_by_title,sort_by_year

def test_year():
    movies = [
    Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    Movie("Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
    Movie("The Matrix", 1999, ["Action", "Sci-Fi"]),
    Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
    Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
    ]
    sorted_by_year = sort_by_year(movies)
    actual=[]
    for movie in sorted_by_year:
        actual.append(f"{movie.title} - {movie.year}")
    expected=['The Matrix - 1999', 'A Beautiful Mind - 2001', 'The Dark Knight - 2008', 'Inception - 2010', 'The Avengers - 2012']
    assert actual==expected


def test_title():
    movies = [
    Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    Movie("Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
    Movie("The Matrix", 1999, ["Action", "Sci-Fi"]),
    Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
    Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
    ]
    sorted_by_year = sort_by_title(movies)
    actual=[]
    for movie in sorted_by_year:
        actual.append(f"{movie.title} - {movie.year}")
    expected=['The Avengers - 2012', 'A Beautiful Mind - 2001', 'The Dark Knight - 2008', 'Inception - 2010', 'The Matrix - 1999']
    assert actual==expected