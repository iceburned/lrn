from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE_INCREASES = 2

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)
        self.inhabited = "SaltwaterAquarium"

    def eat(self):
        self.size += SaltwaterFish.SIZE_INCREASES
