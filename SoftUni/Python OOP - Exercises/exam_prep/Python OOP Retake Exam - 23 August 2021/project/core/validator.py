class Validator:
    @staticmethod
    def return_if_empty_or_whitespace_string(value, message):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def search_by_name(name, astronauts_list):
        searched_astronaut = [_ for _ in astronauts_list if name == _.name]
        if any(searched_astronaut):
            return searched_astronaut

    @staticmethod
    def suitable_astronauts_for_mission(astronauts_list):
        suitable_astronauts = []

        for obj in astronauts_list:
            if obj.oxygen > 30:
                suitable_astronauts.append(obj)

        suitable_astronauts = sorted(suitable_astronauts, key=lambda x: x.oxygen, reverse=True)
        if len(astronauts_list) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        return suitable_astronauts[:5]



