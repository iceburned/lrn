from unittest import TestCase

from project.movie import Movie


class MovieTest(TestCase):
    NAME = "Hard"
    YEAR = 2000
    RATING = 8

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_with_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_year_smaller_than_1887(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1800

        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor_not_existing(self):
        first = "Pesho"
        second = "Gosho"

        self.movie.add_actor(first)
        self.movie.add_actor(second)
        self.assertEqual([first, second], self.movie.actors)

    def test_add_actor_with_duplicated_name(self):
        name = "Pesho"
        self.movie.actors = [name]
        result = self.movie.add_actor(name)

        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)

    def test_gt_(self):
        other_name = "Matrix"
        another_movie = Movie(other_name, 2001, self.RATING - 1)

        first_result = self.movie > another_movie
        second_result = another_movie > self.movie

        self.assertEqual(f'"{self.NAME}" is better than "{other_name}"', first_result)
        self.assertEqual(f'"{self.NAME}" is better than "{other_name}"', second_result)

    def test_repr(self):
        actors = ["Pesho", "Gosho"]
        self.movie.actors = actors
        actual_result = repr(self.movie)
        expected_result = f"Name: {self.NAME}\n" \
               f"Year of Release: {self.YEAR}\n" \
               f"Rating: {self.RATING:.2f}\n" \
               f"Cast: {', '.join(actors)}"

        self.assertEqual(expected_result, actual_result)
