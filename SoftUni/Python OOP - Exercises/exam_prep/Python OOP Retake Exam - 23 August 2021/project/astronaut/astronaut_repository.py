from project.astronaut.astronaut import Astronaut
from project.core.validator import Validator


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        return Validator.search_by_name(name, self.astronauts)
