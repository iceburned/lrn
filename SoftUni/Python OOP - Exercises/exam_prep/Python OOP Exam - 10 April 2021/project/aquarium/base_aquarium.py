from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self._name = value

    def calculate_comfort(self):
        return sum(_.comfort for _ in self.decorations)

    def calculate_fishes_size(self):
        return sum(_.size for _ in self.fish)

    def add_fish(self, fish):
        if self.capacity < self.calculate_fishes_size() + fish.size:
            return "Not enough capacity."
        if fish.inhabited != self.__class__.__name__:
            return "Water not suitable."
        if self.__class__.__name__ == fish.inhabited:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [_.eat() for _ in self.fish]

    def __str__(self):
        names = [_.name for _ in self.fish]
        return f"{self.name}\n" \
               f"Fish: {' '.join(names) if any(names) else 'none'}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
