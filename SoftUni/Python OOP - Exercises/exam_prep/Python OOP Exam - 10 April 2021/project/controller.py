from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []
        self.allowed_aquariums = ["FreshwaterAquarium", "SaltwaterAquarium"]
        self. allowed_decorations = ["Ornament", "Plant"]
        self.allowed_fishes = ["FreshwaterFish", "SaltwaterFish"]

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self.allowed_aquariums:
            return "Invalid aquarium type."
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        else:
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self.allowed_decorations:
            return "Invalid decoration type."
        if decoration_type == "Plant":
            self.decorations_repository.add(Plant())
        else:
            self.decorations_repository.add(Ornament())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        for o in self.aquariums:
            if o.name == aquarium_name:
                answer = self.decorations_repository.find_by_type(decoration_type)
                if answer != "None":
                    o.add_decoration(answer)
                    return f"Successfully added {decoration_type} to {aquarium_name}."
                return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        fish = ''
        if fish_type not in self.allowed_fishes:
            return f"There isn't a fish of type {fish_type}."
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)
        # TODO check if aquarium is present
        for o in self.aquariums:
            if o.name == aquarium_name:
                return o.add_fish(fish)

    def feed_fish(self, aquarium_name):
        for o in self.aquariums:
            if o.name == aquarium_name:
                o.feed()
                return f"Fish fed: {len(o.fish)}"

    def calculate_value(self, aquarium_name):
        for o in self.aquariums:
            if o.name == aquarium_name:
                fishes_price = sum(_.price for _ in o.fish)
                decorations_price = sum(_.price for _ in o.decorations)
                return f"The value of Aquarium {aquarium_name} is {fishes_price + decorations_price:.2f}."

    def report(self):
        for o in self.aquariums:
            return str(o)
