from project.planet.planet import Planet


class PlanetFactory:

    @staticmethod
    def create_planet(name, items):
        items = items.split(", ")
        planet = Planet(name)
        planet.items += items
        return planet
