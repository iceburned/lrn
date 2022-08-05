from project.controller import Controller
from project.core.validator import Validator


class Player:
    _UNDER_AGE = 12
    _LESS_THAN = 0
    _MORE_THAN = 100
    _LESS_THAN_BOOL = 100
    _USED_NAMES = set()

    def __init__(self, name, age, stamina=100):
        self.controller = Controller()
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        if value in self._USED_NAMES:
            raise Exception(f"Name {value} is already used!")
        self._USED_NAMES.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.value_less_than(value,
                                  self._UNDER_AGE,
                                  f"The player cannot be under {self._UNDER_AGE} years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.less_than_or_more_than(value, self._LESS_THAN, self._MORE_THAN, "Stamina not valid!")
        self.__stamina = value
    
    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True
        return False

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
