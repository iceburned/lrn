


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        players = []
        for player in args:
            if player not in self.players:
                players.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join(players)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name, sustenance_type):
        player = self.__player_present(player_name)
        if player is None:
            return
        if player.stamina == 100:
            return f"{player_name} have enough stamina."
        supply = self.__last_supply_taken(sustenance_type)
        if supply:
            player._player_sustain(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = self.__player_present(first_player_name)
        second_player = self.__player_present(second_player_name)
        result = self.__player_can_fight(first_player, second_player)
        if result:
            return result
        if first_player.stamina < second_player.stamina:
            return self.__attack_player(first_player, second_player)
        else:
            return self.__attack_player(second_player, first_player)

    def next_day(self):
        for obj in self.players:
            if obj.stamina - (obj.age * 2) < 0:
                obj.stamina = 0
            else:
                obj.stamina -= (obj.age * 2)
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        answer = []
        for p in self.players:
            answer.append(p.__str__())
        for s in self.supplies:
            answer.append(s.details())
        result = '\n'.join(answer)
        return result

    def __player_present(self, name):
        for obj in self.players:
            if obj.name == name:
                return obj
        return None

    def __last_supply_taken(self, item_type):
        for i in range(len(self.supplies) - 1, -1, -1):
            if type(self.supplies[i]).__name__ == item_type:
                return self.supplies.pop(i)
        if item_type == "Food":
            raise Exception("There are no food supplies left!")
        elif item_type == "Drink":
            raise Exception("There are no drink supplies left!")

    @staticmethod
    def __player_can_fight(*args):
        answer = []
        for obj in args:
            if obj.stamina == 0:
                answer.append(f"Player {obj.name} does not have enough stamina.")
        return '\n'.join(answer)

    @staticmethod
    def __attack_player(p1, p2):
        p2.stamina -= p1.stamina / 2
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= p2.stamina / 2
        if p1.stamina < p2.stamina:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"
