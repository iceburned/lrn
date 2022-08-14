from project.astronaut.astronaut_repository import AstronautRepository
from project.core.astronaut_factory import AstronautFactory
from project.core.planet_factory import PlanetFactory
from project.core.validator import Validator
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.mission_successful = 0
        self.mission_unsuccessful = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        check_for_present_astro = Validator.search_by_name(name, self.astronaut_repository.astronauts)
        if check_for_present_astro is not None:
            return f"{name} is already added."
        AstronautFactory.astronaut_validation_for_type(astronaut_type)
        astronaut = AstronautFactory.create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        check_for_present_planet = Validator.search_by_name(name, self.planet_repository.planets)
        if check_for_present_planet is not None:
            return f"{name} is already added."
        planet = PlanetFactory.create_planet(name, items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        check_for_present_astro = Validator.search_by_name(name, self.astronaut_repository.astronauts)
        if check_for_present_astro is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(check_for_present_astro)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for obj in self.astronaut_repository.astronauts:
            obj.oxygen += 10

    def send_on_mission(self, planet_name: str):
        check_for_present_planet = Validator.search_by_name(planet_name, self.planet_repository.planets)
        if check_for_present_planet is None:
            raise Exception("Invalid planet name!")
        items_to_collect = check_for_present_planet[0].items
        suitable_astronauts = Validator.suitable_astronauts_for_mission(self.astronaut_repository.astronauts)
        if len(suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        count_astro = 0
        flag = False
        for obj in suitable_astronauts:

            if len(items_to_collect) == 0:
                break
            while obj.oxygen > 0 or len(items_to_collect) > 0:
                item = items_to_collect.pop()
                obj.backpack.append(item)
                obj.breathe()
            count_astro += 1
        if flag:
            self.mission_successful += 1
            return f"Planet: {planet_name} was explored. {count_astro} astronauts " \
                   f"participated in collecting items."
        self.mission_unsuccessful += 1
        return "Mission is not completed."

    def report(self):
        return f"Astronauts' info:\n"\
               f"{self.mission_successful} successful missions!\n" \
               f"{self.mission_unsuccessful} missions were not completed!\n" \
               f"{''.join(obj.info for obj in self.astronaut_repository.astronauts)}"
