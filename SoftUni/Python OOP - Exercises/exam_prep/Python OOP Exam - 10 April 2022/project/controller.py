from project.core.validator import Validator


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        lst = []
        for el in args:
            if el in self.players:
                continue
            self.players.append(el)
            lst.append(el)
        return f"Successfully added: {', '.join([_.name for _ in lst])}"

    def add_supply(self, *args):
        for el in args:
            self.supplies.append(el)

    def sustain(self, player_name: str, sustenance_type: str):
        allowed_sustenance_type = ["Food", "Drink"]
        player = Validator.find_by_name(player_name, self.players)
        if player is None:
            return
        if not player.need_sustenance:
            return f"{player.name} have enough stamina."
        if sustenance_type not in allowed_sustenance_type:
            return
        last_supply = Validator.last_supply_from_same_type(sustenance_type, self.supplies)
        if last_supply is None:
            return f"There are no {sustenance_type} supplies left!"
        player.stamina = min(player.stamina + last_supply.energy, 100)
        for _ in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[_] == last_supply:
                self.supplies.pop(_)
                break
        return f"{player_name} sustained successfully with {last_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = Validator.find_by_name(first_player_name, self.players)
        player2 = Validator.find_by_name(second_player_name, self.players)
        stamina_check_player1 = Validator.stamina_less_than(player1.stamina,
                                                            1,
                                                            f"Player {player1.name} does not have enough stamina.")
        stamina_check_player2 = Validator.stamina_less_than(player2.stamina,
                                                            1,
                                                            f"Player {player2.name} does not have enough stamina.")
        if stamina_check_player1 is not None:
            return stamina_check_player1
        if stamina_check_player2 is not None:
            return stamina_check_player2
        order_of_attack = [player1, player2]
        first, second = sorted(order_of_attack, key=lambda x: x.stamina)
        second.stamina = second.stamina - first.stamina / 2
        if first.stamina <= 0:
            first.stamina = 0
            return f"Winner: {second.name}"
        first.stamina = first.stamina - second.stamina / 2
        if second.stamina <= 0:
            second.stamina = 0
            return f"Winner: {first.name}"
        winner = first if first.stamina > second.stamina else second
        return f"Winner: {winner.name}"

    def next_day(self):
        for el in self.players:
            stamina = el.stamina
            age = el.age
            if el.stamina - (age * 2) <= 0:
                el.stamina = 0
            else:
                el.stamina = stamina - (age * 2)
            self.sustain(el.name, "Food")
            self.sustain(el.name, "Drink")

    def __str__(self):
        lst = ''
        for el in self.players:
            lst += str(el) + "\n"
        for el in self.supplies:
            lst += el.details() + "\n"
        return lst
