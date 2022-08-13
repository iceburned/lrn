from unittest import TestCase

from project.train.train import Train


class TrainTest(TestCase):

    def setUp(self) -> None:
        self.train = Train("Fast", 2)

    def test_init(self):
        self.assertEqual("Fast", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertListEqual([], self.train.passengers)

    def test_add_passenger_if_full(self):
        self.train.passengers = ["Pesho", "Gosho"]
        with self.assertRaises(ValueError) as error:
            self.train.add("Ivan")
        self.assertEqual("Train is full", str(error.exception))

    def test_add_passenger_if_person_in_train(self):
        self.train.passengers = ["Pesho"]
        with self.assertRaises(ValueError) as error:
            self.train.add("Pesho")
        self.assertEqual("Passenger Pesho Exists", str(error.exception))

    def test_add_passenger(self):
        self.train.passengers = ["Pesho"]
        answer = self.train.add("Gosho")
        self.assertEqual(["Pesho", "Gosho"], self.train.passengers)
        self.assertEqual("Added passenger Gosho", answer)

    def test_remove_passenger(self):
        self.train.add("Pesho")
        self.train.add("Gosho")
        with self.assertRaises(ValueError) as error:
            self.train.remove("Ivan")
        self.assertEqual("Passenger Not Found", str(error.exception))

    def test_remove_missing_passenger(self):
        self.train.add("Pesho")
        self.train.add("Gosho")
        self.train.remove("Pesho")
        self.assertEqual(["Gosho"], self.train.passengers)

    def test_remove_missing_passenger_message(self):
        self.train.add("Pesho")
        self.train.add("Gosho")
        answer = self.train.remove("Pesho")
        self.assertEqual("Removed Pesho", answer)
