from project.library import Library
from unittest import TestCase


class LibraryTest(TestCase):
    NAME = "Varna"
    AUTHOR = "Oscar"
    TITLE = "Star Wars"

    def setUp(self) -> None:
        self.library = Library("Varna")

    def test_init(self):
        self.assertEqual(self.library.name, self.NAME)
        self.assertDictEqual({}, self.library.books_by_authors)
        self.assertDictEqual({}, self.library.readers)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as error:
            Library("")
        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test_add_book_if_author_not_exist(self):
        self.library.add_book("Ivan", "Zima")
        self.assertEqual({"Ivan": ["Zima"]}, self.library.books_by_authors)

    def test_add_title_if_not_exist(self):
        self.library.add_book("Ivan", "Winter")
        self.library.add_book("Ivan", "Spring")
        self.assertEqual({"Ivan": ["Winter", "Spring"]}, self.library.books_by_authors)

    def test_add_title_if_exist(self):
        self.library.add_book("Ivan", "Winter")
        self.library.add_book("Ivan", "Winter")
        self.assertEqual({"Ivan": ["Winter"]}, self.library.books_by_authors)

    def test_add_reader_if_not_exist(self):
        self.library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, self.library.readers)

    def test_add_reader_if_exist(self):
        self.library.add_reader("Ivan")
        answer = self.library.add_reader("Ivan")
        self.assertEqual("Ivan is already registered in the Varna library.", answer)

    def test_rent_book_with_no_existing_reader(self):
        answer = self.library.rent_book("Ivan", "Gosho", "Star Wars")
        self.assertEqual("Ivan is not registered in the Varna Library.", answer)

    def test_book_author_not_exist(self):
        self.library.readers = {"Ivan": []}
        answer = self.library.rent_book("Ivan", "Gosho", "Star Wars")
        self.assertEqual("Varna Library does not have any Gosho's books.", answer)

    def test_title_not_in_author_books(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Gosho": []}
        answer = self.library.rent_book("Ivan", "Gosho", "Star Wars")
        self.assertEqual("""Varna Library does not have Gosho's "Star Wars".""", answer)

    def test_rent_book_with_existing_reader_author_title(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Gosho": ["Star Wars"]}
        answer = self.library.rent_book("Ivan", "Gosho", "Star Wars")
        self.assertEqual({"Ivan": [{"Gosho": "Star Wars"}]}, self.library.readers)
