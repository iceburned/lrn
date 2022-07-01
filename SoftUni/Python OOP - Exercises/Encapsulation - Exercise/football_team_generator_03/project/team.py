from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        for s in self.__players:
            if s.name == player.name:
                return f"Player {player.name} has already joined"
            else:
                self.__players.append(s(player))
                return f"Player {player.name} joined team {self.__name}"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for s in self.__players:
            if s.name == player_name:
                self.__players.remove(s)
                return s
        return f"Player {player_name} not found"
