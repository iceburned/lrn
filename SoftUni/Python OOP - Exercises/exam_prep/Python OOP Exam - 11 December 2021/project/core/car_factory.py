from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:
    car_types = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def car_creation(self, car_type, model, speed_limit):
        if car_type not in self.car_types:
            raise RuntimeError("Invalid car type")
        return self.car_types[car_type](model, speed_limit)

