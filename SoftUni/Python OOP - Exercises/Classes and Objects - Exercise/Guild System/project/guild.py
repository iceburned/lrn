from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for plr in self.players:
            if plr.name == player_name:
                plr.guild = "Unaffiliated"
                self.players.remove(plr)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        guild_name = f"Guild: {self.name}"
        player_name = [_.player_info() for _ in self.players]
        return guild_name + "\n" + '\n'.join(player_name)
