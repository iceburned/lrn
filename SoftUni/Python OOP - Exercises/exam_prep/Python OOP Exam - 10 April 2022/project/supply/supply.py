from abc import ABC, abstractmethod

from project.core.validator import Validator


class Supply(ABC):
    _LESS_THAN_NUM = 0

    @abstractmethod
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.value_empty_string(value, "Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):  # if less than zero
        Validator.value_less_than(value, self._LESS_THAN_NUM, "Energy cannot be less than zero.")
        self.__energy = value

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
