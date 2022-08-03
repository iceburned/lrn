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
            car = self.car_factory.car_creation(car_type, model, speed_limit)
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
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        return driver.change_car(car)

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception( f"Race {race_name} could not be found!")

        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        driver_have_been_on_race = self.__driver_already_participate_in_race(race_name, driver_name)
        if driver_have_been_on_race is not None:
            return driver_have_been_on_race  # Driver {driver_name} is already added in {race_name} race.

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        all_winners = ""
        winners = self.__first_3_winners_of_race(race)
        for winner in winners:
            winner.number_of_wins += 1
            all_winners += f"Driver {winner.name} wins the {race.name} race with a speed of {winner.car.speed_limit}.\n"
        return all_winners





    def __find_driver_by_name(self, driver_name):
        for obj in self.drivers:
            if obj.name == driver_name:
                return obj
        return None

    def __find_car_by_type(self, car_type):
        for index in range(len(self.cars) - 1, -1, -1):
            car = self.cars[index]
            if car.__class__.__name__ == car_type and car.is_taken is False:
                return car
        return None

    def __find_race_by_name(self, race_name):
        for obj in self.races:
            if race_name == obj.name:
                return obj
        return None

    def __driver_already_participate_in_race(self, race_name, driver_name):
        for obj in self.races:
            for driver in obj.drivers:
                if driver.name == driver_name:
                    return f"Driver {driver_name} is already added in {race_name} race."
        return None

    def __first_3_winners_of_race(self, race):
        drivers = race.drivers
        racing = sorted(drivers, key=lambda x: -x.car.speed_limit)
        return racing[:3]
