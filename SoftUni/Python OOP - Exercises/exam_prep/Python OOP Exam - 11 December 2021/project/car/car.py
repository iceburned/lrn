from abc import ABC, abstractmethod

from project.core.validator import Validator


class Car(ABC):
    @abstractmethod
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.string_should_be_no_less_than_4_characters(value,
                                f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.speed_limiter(value,
                                self.min_speed_limit,
                                self.max_speed_limit,
                                f"Invalid speed limit! Must be between {self.min_speed_limit} and "
                                f"{self.max_speed_limit}!")
        self.__speed_limit = value

    @property
    @abstractmethod
    def min_speed_limit(self):
        pass

    @property
    @abstractmethod
    def max_speed_limit(self):
        pass
