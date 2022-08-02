from project.core.car_factory import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []
        self.car_factory = CarFactory()

    def create_car(self, car_type, model, speed_limit):
        if any(_.model == model for _ in self.cars):
            raise Exception(f"Car {model} is already created!")
        try:
            car = self.car_factory.car_creation(car_type, model,  speed_limit)
            self.cars.append(car)
            return f"{car.__class__.__name__} {car.model} is created."
        except RuntimeError:
            pass

    def create_driver(self, driver_name: str):
        if any(_.name == driver_name for _ in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver.name} is created."

    def create_race(self, race_name):
        if any(_.name == race_name for _ in self.races):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race.name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        # driver = Validator.same_name_like_object_name(driver_name, self.drivers)
        # reversed_cars = reversed(self.cars)
        # car = Validator.same_model_like_object_model(car_type, reversed_cars)
        # if any(driver):
        #     raise Exception(f"Driver {driver_name} could not be found!")
        # if any(car):
        #     raise Exception(f"Car {car_type} could not be found!")
        pass

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name):
        pass

#
# c = Controller()
# c.create_car("MuscleCar", "Ford", 400)
# a = 1
