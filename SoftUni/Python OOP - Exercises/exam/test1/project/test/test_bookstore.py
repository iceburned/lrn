from project.bookstore import Bookstore

from unittest import TestCase


class BookstoreTest(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(3)

    def test_init(self):
        self.assertEqual(3, self.bookstore.books_limit)
        self.assertDictEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_book_limit_setter_is_zero(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(error.exception))

    def test_book_limit_setter_is_less_than_zero(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = -1
        self.assertEqual("Books limit of -1 is not valid", str(error.exception))

    def test_book_limit_setter_is_passing(self):
        self.bookstore.books_limit = 3
        self.assertEqual(3, self.bookstore.books_limit)

    def test_len(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 2, "B": 1}
        answer = self.bookstore.__len__()
        self.assertEqual(3, answer)

    def test_receive_book_limit(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 2}
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book("C", 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_not_exist(self):
        self.bookstore.receive_book("A", 2)
        actual = self.bookstore.availability_in_store_by_book_titles
        self.assertEqual({"A": 2}, actual)

    def test_receive_book_not_exist_with_other_existing(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 1}
        self.bookstore.receive_book("B", 2)
        actual = self.bookstore.availability_in_store_by_book_titles
        self.assertEqual({"A": 1, "B": 2}, actual)

    def test_receive_book_if_exist(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 1}
        self.bookstore.receive_book("A", 1)
        actual = self.bookstore.availability_in_store_by_book_titles
        self.assertEqual({"A": 2}, actual)

    def test_receive_book_return_info(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 1}
        actual = self.bookstore.receive_book("A", 1)
        self.assertEqual("2 copies of A are available in the bookstore.", actual)

    def test_sell_book_not_exist(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("A", 2)
        self.assertEqual("Book A doesn't exist!", str(error.exception))

    def test_sell_book_exist_with_less_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 1}
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("A", 2)
        self.assertEqual("A has not enough copies to sell. Left: 1", str(error.exception))

    def test_sell_book_exist(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 2}
        actual = self.bookstore.sell_book("A", 1)
        self.assertEqual("Sold 1 copies of A", actual)

    def test_sell_book_exist_check_how_much_copies_left(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 2}
        self.bookstore.sell_book("A", 1)
        self.assertEqual({"A": 1}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_exist_check_total_sold_books(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 2}
        self.bookstore.sell_book("A", 1)
        self.assertEqual(1, self.bookstore.total_sold_books)

    def test_str(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 2, "B": 1}
        actual = self.bookstore.__str__()
        expected = 'Total sold books: 0\nCurrent availability: 3\n - A: 2 copies\n - B: 1 copies'
        self.assertEqual(expected, actual)
