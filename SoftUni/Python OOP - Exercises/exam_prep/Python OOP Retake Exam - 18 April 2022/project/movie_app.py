from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if self.__name_in_lst(username, self.users_collection):
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if not self.__name_in_lst(username, self.users_collection):
            raise Exception("This user does not exist!")
        elif not self.__movie_in_lst(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        elif movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        else:
            user = self.user_in_list(username, self.users_collection)
            user.movies_owned.append(movie)
            self.movies_collection.append(movie)
            return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.__movie_in_lst(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        elif not self.__movie_in_lst(username, movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        else:
            self.__change_attributes_of_movie(movie, kwargs)
            return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not self.__movie_in_lst(username, movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif not self.__movie_in_lst(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        else:
            title = movie.title
            user = self.user_in_list(username, self.users_collection)
            user.movies_owned.remove(movie)
            self.movies_collection.remove(movie)
            return f"{username} successfully deleted {title} movie."

    def like_movie(self, username: str, movie: Movie):
        if self.__movie_in_lst(username, movie):
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        user = self.user_in_list(username, self.users_collection)
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.user_in_list(username, self.users_collection)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        movies = sorted(self.movies_collection, key=lambda x: (x.year, x.title), reverse=True)
        if len(movies) <= 0:
            return "No movies found."
        all_movies = []
        for obj in movies:
            all_movies.append(obj.details())
        return '\n'.join(all_movies)

    def __str__(self):
        result = "All users: "
        if len(self.users_collection) <= 0:
            result += "No users."
        else:
            result += ', '.join([_.username for _ in self.users_collection])
        result_2 = "All movies: "
        if len(self.movies_collection) <= 0:
            result_2 += "No movies."
        else:
            result_2 += ', '.join([_.title for _ in self.movies_collection])
        return result + "\n" + result_2


    @staticmethod
    def __name_in_lst(username, collection):
        for obj in collection:
            if obj.username == username:
                return True
        return False

    @staticmethod
    def __movie_in_lst(username, movie):
        if username == movie.owner.username:
            return True
        return False

    @staticmethod
    def user_in_list(user, collection):
        for el in collection:
            if el.username == user:
                return el

    @staticmethod
    def __change_attributes_of_movie(movie, kwargs):
        for k, v in kwargs.items():
            setattr(movie, k, v)
        return movie

