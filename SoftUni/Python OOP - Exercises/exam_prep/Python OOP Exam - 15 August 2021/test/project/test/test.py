from project.pet_shop import PetShop

from unittest import TestCase


class PetShopTest(TestCase):

    def setUp(self) -> None:
        self.pet_shop = PetShop("Forever")

    def test_init(self):
        self.assertEqual("Forever", self.pet_shop.name)
        self.assertDictEqual({}, self.pet_shop.food)
        self.assertListEqual([], self.pet_shop.pets)

    def test_add_food_less_than_zero(self):
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food("bread", -2.0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_when_food_name_does_not_exist(self):
        self.pet_shop.add_food("Bread", 2.0)
        self.assertEqual({"Bread": 2.0}, self.pet_shop.food)

    def test_add_food_when_food_name_exist(self):
        self.pet_shop.food = {"Bread": 4.0}
        self.pet_shop.add_food("Bread", 2.0)
        self.assertEqual({"Bread": 6.0}, self.pet_shop.food)

    def test_add_food_when_food_name_does_not_exist_to_return_message(self):
        answer = self.pet_shop.add_food("Bread", 2.0)
        self.assertEqual("Successfully added 2.00 grams of Bread.", answer)

    def test_add_pet_if_not_exist(self):
        self.pet_shop.add_pet("Cudjo")
        self.assertEqual(["Cudjo"], self.pet_shop.pets)

    def test_add_pet_if_not_exist_message(self):
        answer = self.pet_shop.add_pet("Cudjo")
        self.assertEqual("Successfully added Cudjo.", answer)

    def test_add_pet_when_pet_exist(self):
        self.pet_shop.add_pet("Cudjo")
        with self.assertRaises(Exception) as error:
            self.pet_shop.add_pet("Cudjo")
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test_feed_up_when_pet_does_not_exist(self):
        self.pet_shop.add_pet("Cudjo")
        with self.assertRaises(Exception) as error:
            self.pet_shop.feed_pet("Bread", "Sharo")
        self.assertEqual("Please insert a valid pet name", str(error.exception))

    def test_feed_pet_when_unknown_food(self):
        self.pet_shop.add_pet("Cudjo")
        self.pet_shop.add_food("Bread", 2.0)
        answer = self.pet_shop.feed_pet("Salami", "Cudjo")
        self.assertEqual('You do not have Salami', answer)

    def test_feed_pet_adding_food_less_than_100_message(self):
        self.pet_shop.add_pet("Cudjo")
        self.pet_shop.add_food("Bread", 2.0)
        answer = self.pet_shop.feed_pet("Bread", "Cudjo")
        self.assertEqual("Adding food...", answer)

    def test_feed_pet_adding_food_less_than_100_update_value(self):
        self.pet_shop.add_pet("Cudjo")
        self.pet_shop.add_food("Bread", 2.0)
        self.pet_shop.feed_pet("Bread", "Cudjo")
        self.assertEqual({"Bread": 1002.00}, self.pet_shop.food)

    def test_fed_pet_successfully_fed(self):
        self.pet_shop.add_pet("Cudjo")
        self.pet_shop.add_food("Bread", 500.00)
        answer = self.pet_shop.feed_pet("Bread", "Cudjo")
        self.assertEqual("Cudjo was successfully fed", answer)
        self.assertEqual({"Bread": 400.00}, self.pet_shop.food)

    def test_repr(self):
        self.pet_shop.add_pet("Cudjo")
        self.pet_shop.add_pet("Sharo")
        actual = self.pet_shop.__repr__()
        expexted = 'Shop Forever:\n' \
               'Pets: Cudjo, Sharo'
        self.assertEqual(expexted, actual)
