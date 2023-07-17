
class Movie:
    """
    Represents a movie with its title, year, and genres.

    Attributes:
        title (str): The title of the movie.
        year (int): The year of release.
        genres (list): The genres associated with the movie.

    Methods:
        __init__(title, year, genres):
            Initializes a new instance of the Movie class.

    """
    def __init__(self, title, year, genres):
        """
        Initializes a new instance of the Movie class.

        Parameters:
            title (str): The title of the movie.
            year (int): The year of release.
            genres (list): The genres associated with the movie.

        Returns:
            None

        Description:
            This constructor initializes a new instance of the Movie class with the provided title, year, and genres.
            The attributes 'title', 'year', and 'genres' are assigned the corresponding values.
        """
        self.title = title
        self.year = year
        self.genres = genres

def sort_by_year(movies):
    """
    Sorts a list of movies based on the year of release.

    Parameters:
        movies (list): A list of Movie objects.

    Returns:
        list: The sorted list of movies.

    Description:
        This function takes a list of Movie objects and sorts them based on the year of release in descending order.
        It uses the 'sorted' function with a lambda function as the key parameter to specify the sorting criteria.
        The sorted list of movies is returned.
    """
    return sorted(movies, key=lambda movie: movie.year)

def sort_by_title(movies):
    """
    Sorts a list of movies based on the movie titles.

    Parameters:
        movies (list): A list of Movie objects.

    Returns:
        list: The sorted list of movies.

    Description:
        This function takes a list of Movie objects and sorts them based on the movie titles.
        It uses the 'sorted' function with a lambda function as the key parameter to specify the sorting criteria.
        The lambda function calls the 'get_title_without_prefix' helper function to remove common title prefixes
        ('A ', 'An ', 'The ') for more accurate sorting.
        The sorted list of movies is returned.
    """
    def get_title_without_prefix(title):
        """
        Removes common title prefixes from a movie title.

        Parameters:
            title (str): The movie title.

        Returns:
            str: The movie title without the common prefixes.

        Description:
            This helper function takes a movie title as input and removes common title prefixes ('A ', 'An ', 'The ')
            from the beginning of the title. If no prefix is found, the original title is returned.
        """
        prefix = ["A ", "An ", "The "]
        for p in prefix:
            if title.startswith(p):
                return title[len(p):]
        return title

    return sorted(movies, key=lambda movie: get_title_without_prefix(movie.title))


# Test data
movies = [
    Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    Movie("Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
    Movie("The Matrix", 1999, ["Action", "Sci-Fi"]),
    Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
    Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
]

# Test sorting by year
sorted_by_year = sort_by_year(movies)
print("Sorted by year:")
li=[]
for movie in sorted_by_year:
   li.append(f"{movie.title} - {movie.year}")
print(li)