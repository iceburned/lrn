class Validator:
    @staticmethod
    def return_if_empty_or_whitespace_string(value, message):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def search_by_name(name, astronauts_list):
        searched = [_ for _ in astronauts_list if name == _.name]
        if any(searched):
            return searched

    @staticmethod
    def suitable_astronauts_for_mission(astronauts_list):
        suitable_astronauts = []

        for obj in astronauts_list:
            if obj.oxygen > 30 or len(suitable_astronauts) < 5:
                suitable_astronauts.append(obj)

        suitable_astronauts = sorted(suitable_astronauts, key=lambda x: x.oxygen, reverse=True)

        return suitable_astronauts



