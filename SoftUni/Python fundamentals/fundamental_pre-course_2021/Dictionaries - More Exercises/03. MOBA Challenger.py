dkt = {}
data = input()

while not data == "Season end":
    if "->" in data:
        player, position, skill = data.split(" -> ")
        skill = int(skill)
        if player not in dkt:
            dkt[player] = {}
        if position not in dkt[player]:
            dkt[player][position] = skill
        else:
            if dkt[player][position] < skill:
                dkt[player][position] = skill
    elif "vs" in data:
        player1, player2 = data.split(" vs ")
        if player1 in dkt and player2 in dkt:
            for role in dkt[player1].keys():
                if role in dkt[player2]:
                    plr1 = sum(dkt[player1].values())
                    plr2 = sum(dkt[player2].values())
                    if plr1 > plr2:
                        dkt.pop(player2)
                        break
                    elif plr1 < plr2:
                        dkt.pop(player1)
                        break
    data = input()

for name, place_and_p in sorted(dkt.items(), key=lambda b: (-sum(b[1].values()), b[0])):
    print(f'{name}: {sum(place_and_p.values())} skill')
    for place, p in sorted(place_and_p.items(), key=lambda n: (-int(n[1]), n[0])):
        print(f'- {place} <::> {p}')
