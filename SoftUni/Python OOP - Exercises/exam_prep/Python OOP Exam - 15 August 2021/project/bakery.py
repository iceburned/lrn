from project.core.drink_factory import DrinkFactory
from project.core.food_factory import FoodFactory
from project.core.table_factory import TableFactory
from project.core.validator import Validator


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0
        self.food_factory = FoodFactory()
        self.drink_factory = DrinkFactory()
        self.table_factory = TableFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(
            value,
            "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        if any(_.name == name for _ in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = self.food_factory.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if any(_.name == name for _ in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = self.drink_factory.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any(_.table_number == table_number for _ in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = self.table_factory.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):  # table
        table = [_ for _ in self.tables_repository if not _.is_reserved and number_of_people <= _.capacity]
        if any(table):
            obj = table[0]
            obj.reserve(number_of_people)
            return f"Table {obj.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        table = self.find_table_by_number(table_number)
        if not any(table):
            return f"Could not find table {table_number}"
        table_obj = table[0]
        in_menu = []
        not_in_menu = []

        for el in args:
            for o in self.food_menu:
                if el == o.name:
                    table_obj.order_food(o)
                    in_menu.append(repr(o))
                    break
            else:
                not_in_menu.append(el)
        menu = '\n'.join(in_menu)
        not_menu = '\n'.join(not_in_menu)
        return f"Table {table_number} ordered:\n" \
               f"{menu}\n" \
               f"{self.name} does not have in the menu:\n" \
               f"{not_menu}\n"

    def order_drink(self, table_number, *args):
        table = self.find_table_by_number(table_number)
        if not any(table):
            return f"Could not find table {table_number}"
        table_obj = table[0]
        in_menu = []
        not_in_menu = []

        for el in args:
            for o in self.drinks_menu:
                if el == o.name:
                    table_obj.order_drink(o)
                    in_menu.append(repr(o))
                    break
            else:
                not_in_menu.append(el)
        menu = '\n'.join(in_menu)
        not_menu = '\n'.join(not_in_menu)
        return f"Table {table_number} ordered:\n" \
               f"{menu}\n" \
               f"{self.name} does not have in the menu:\n" \
               f"{not_menu}\n"

    def leave_table(self, table_number):
        table = self.find_table_by_number(table_number)
        table_obj = table[0]
        bill = table_obj.get_bill()
        self.total_income += bill
        table_obj.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        lst = [o.free_table_info() for o in self.tables_repository if not o.free_table_info() is None]
        return '\n'.join(lst)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def find_table_by_number(self, table_number):
        return [_ for _ in self.tables_repository if table_number == _.table_number]

#
# b = Bakery("bakery")
# print(b.add_food("Bread", "Carrot", 1.5))
# print(b.add_drink("Tea", "Lemon", 1.5, "broodmare"))
# print(b.add_table("OutsideTable", 60, 5))
# print(b.add_table("InsideTable", 10, 10))
# print(b.reserve_table(4))
# print(b.order_food(10, "Carrot"))
# print(b.get_free_tables_info())
# print(b.total_income)
# print(b.leave_table(10))

