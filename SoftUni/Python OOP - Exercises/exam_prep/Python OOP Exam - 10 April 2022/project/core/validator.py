class Validator:

    @staticmethod
    def value_empty_string(value, message):
        if value == "":
            raise ValueError(message)

    @staticmethod
    def value_less_than(value, num, message):
        if value < num:
            raise ValueError(message)

    @staticmethod
    def stamina_less_than(value, num, message):
        if value < num:
            return message
        return None

    @staticmethod
    def name_already_in_list(name, players_list, message):
        for player in players_list:
            if player.name == name:
                raise Exception(message)

    @staticmethod
    def less_than_or_more_than(num, less_than, more_than, message):
        if not less_than <= num <= more_than:
            raise ValueError(message)

    @staticmethod
    def find_by_name(name, lst_names):
        for el in lst_names:
            if el.name == name:
                return el
        return None

    @staticmethod
    def last_supply_from_same_type(supply, lst_supplys):
        for idx in range(len(lst_supplys) - 1, -1, -1):
            el = lst_supplys[idx]
            if supply == el.__class__.__name__:
                return el
        return None

    @staticmethod
    def supply_from_same_type(supply, lst_supplys):
        for s in lst_supplys:
            if supply == s.__class__.__name__:
                return s
        return None
