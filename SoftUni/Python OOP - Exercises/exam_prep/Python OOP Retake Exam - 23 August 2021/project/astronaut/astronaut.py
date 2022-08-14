from abc import ABC, abstractmethod

from project.core.validator import Validator


class Astronaut(ABC):
    OXYGEN_DECREASE = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.return_if_empty_or_whitespace_string(
            value,
            "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE

    def increase_oxygen(self, amount):
        self.oxygen += amount

    @property
    def info(self):
        bag = ', '.join(self.backpack) if len(self.backpack) != 0 else "none"
        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {bag}\n"
