from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautFactory:

    @staticmethod
    def create_astronaut(job_type, name):
        astro_types = {
            "Biologist": Biologist,
            "Geodesist": Geodesist,
            "Meteorologist": Meteorologist
        }
        return astro_types[job_type](name)

    @staticmethod
    def astronaut_validation_for_type(job_type):
        astro_types = ["Biologist", "Geodesist", "Meteorologist"]
        if job_type not in astro_types:
            raise Exception("Astronaut type is not valid!")
