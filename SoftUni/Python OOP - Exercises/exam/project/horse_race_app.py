from project.core.validator import Validator
from project.horse_race import HorseRace
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = Validator.create_horse(horse_type, horse_name, horse_speed)
        if not horse:
            return horse
        name_exist = any(horse.name == _.name for _ in self.horses)
        if name_exist:
            raise Exception(f"Horse {horse_name} has been already added!")
        else:
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = Jockey(jockey_name, age)
        if not jockey:
            return Jockey
        name_exist = any(jockey_name == _.name for _ in self.jockeys)
        if name_exist:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        else:
            self.jockeys.append(jockey)
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race_type_exist = any(race_type == _.race_type for _ in self.horse_races)
        if race_type_exist:
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        if not race:
            return race
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey_exist = ''
        for ss in self.jockeys:
            if jockey_name == ss.name:
                jockey_exist = ss
                break
        if jockey_exist == '':
            raise Exception(f"Jockey {jockey_name} could not be found!")
        last_horse = Validator.last_horse(horse_type, self.horses)
        if not last_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey_exist.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey_exist.horse = last_horse
        return f"Jockey {jockey_name} will ride the horse {last_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race_exist = ''
        for obj in self.horse_races:
            if obj.race_type == race_type:
                race_exist = obj
                break
        if race_exist == '':
            raise Exception(f"Race {race_type} could not be found!")

        jockey_exist = ''
        for ss in self.jockeys:
            if jockey_name == ss.name:
                jockey_exist = ss
                break

        if jockey_exist == '':
            raise Exception(f"Jockey {jockey_name} could not be found!")
        elif jockey_exist.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        elif jockey_exist in race_exist.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        else:
            race_exist.jockeys.append(jockey_exist)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race_exist = ''
        for obj in self.horse_races:
            if obj.race_type == race_type:
                race_exist = obj
                break
        if race_exist == '':
            raise Exception(f"Race {race_type} could not be found!")
        elif len(race_exist.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        jockeys = race_exist.jockeys
        asd = list(sorted(jockeys, key=lambda x: -x.horse.speed))
        winner = asd[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h " \
               f"is {winner.name}! Winner's horse: {winner.horse.name}."
