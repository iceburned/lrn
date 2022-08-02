from project.core.validator import Validator


class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_or_white_space(value,
                                                 "Name should contain at least one character!")
        self.__name = value
