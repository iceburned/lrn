from unittest import TestCase

from project.factory.paint_factory import PaintFactory


class FactoryTest(TestCase):

    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Color", 3)

    def test_init(self):
        self.assertEqual("Color", self.paint_factory.name)
        self.assertEqual(3, self.paint_factory.capacity)
        self.assertDictEqual({}, self.paint_factory.ingredients)
        self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_can_add_equal_zero(self):
        answer = self.paint_factory.can_add(3)
        self.assertTrue(answer)

    def test_can_add_bigger_than_zero(self):
        answer = self.paint_factory.can_add(1)
        self.assertTrue(answer)

    def test_can_add_equal_less_than_zero(self):
        answer = self.paint_factory.can_add(4)
        self.assertFalse(answer)

    def test_add_ingredient_when_product_not_in_ingredient(self):
        with self.assertRaises(TypeError) as error:
            self.paint_factory.add_ingredient("black", 2)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(error.exception))

    def test_can_add_equal_less_than_zero_message(self):
        with self.assertRaises(ValueError) as error:
            self.paint_factory.add_ingredient("blue", 10)
        self.assertEqual("Not enough space in factory", str(error.exception))

    def test_add_ingredient_not_in_ingredients(self):
        self.paint_factory.add_ingredient("blue", 2)
        self.assertEqual({"blue": 2}, self.paint_factory.ingredients)

    def test_add_ingredient_in_ingredients(self):
        self.paint_factory.add_ingredient("blue", 2)
        self.paint_factory.add_ingredient("blue", 1)
        self.assertEqual({"blue": 3}, self.paint_factory.ingredients)

    def test_remove_ingredient_when_product_not_present(self):
        with self.assertRaises(KeyError) as error:
            self.paint_factory.remove_ingredient("black", 1)
        self.assertEqual("'No such ingredient in the factory'", str(error.exception))

    def test_remove_ingredient_when_product_present_less_than_zero(self):
        self.paint_factory.ingredients = {"blue": 1}
        with self.assertRaises(ValueError) as error:
            self.paint_factory.remove_ingredient("blue", 4)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(error.exception))

    def test_remove_ingredient_when_product_present_equals_zero(self):
        self.paint_factory.ingredients = {"blue": 1}
        self.paint_factory.remove_ingredient("blue", 1)
        self.assertEqual({"blue": 0}, self.paint_factory.ingredients)

    def test_remove_ingredient_when_product_present(self):
        self.paint_factory.ingredients = {"blue": 3}
        self.paint_factory.remove_ingredient("blue", 1)
        self.assertEqual({"blue": 2}, self.paint_factory.ingredients)

    def test_property_products(self):
        self.assertEqual(self.paint_factory.ingredients, self.paint_factory.products)

    def test_repr(self):
        self.paint_factory.ingredients = {"blue": 2, "green": 1}
        actual = self.paint_factory.__repr__()
        expected = "Factory name: Color with capacity 3.\n" \
                   "blue: 2\n" \
                   "green: 1\n"
        self.assertEqual(expected, actual)
