# from project.baked_food.bread import Bread
# from project.baked_food.cake import Cake
# from project.drink.tea import Tea
# from project.drink.water import Water
# from project.table.inside_table import InsideTable
# from project.table.outside_table import OutsideTable


class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_zero_or_negative(num, message):
        if num <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_not_in_range(num: int, min_value, max_value, message):
        if num < min_value or num > max_value:
            raise ValueError(message)


# def food_func_create(food_type: str, name: str, price: float):
#     dkt = {
#         "Bread": Bread,
#         "Cake": Cake
#     }
#     return dkt[food_type](name, price)
#
#
# def drink_func_create(drink_type, name, portion, brand):
#     dkt = {
#         "Tea": Tea,
#         "Water": Water
#     }
#     return dkt[drink_type](name, portion, brand)
#
#
# def table_obj_create(table_type, table_number, capacity):
#     dkt = {
#         "InsideTable": InsideTable,
#         "OutsideTable": OutsideTable
#     }
#     return dkt[table_type](table_number, capacity)
