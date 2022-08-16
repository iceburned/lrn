from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class Validator:

    @staticmethod
    def create_horse(horse_type, name, speed):
        allowed_types = {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred
        }
        if horse_type in allowed_types:
            horsy = allowed_types[horse_type](name, speed)
            return horsy
        else:
            return False

    @staticmethod
    def last_horse(horse_type, horses):
        for i in range(len(horses) - 1, -1, -1):
            if horses[i].__class__.__name__ == horse_type and not horses[i].is_taken:
                return horses[i]
        return False
