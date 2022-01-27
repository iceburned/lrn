winners = {"shards": 0, "fragments": 0, "motes": 0}
item = ''
dkt = {}
while item == '':
    data = input().split(' ')
    material = ''
    quant = 0
    for _ in range(0, len(data), 2):
        quant = int(data[_])
        material = data[_ + 1]
        material = material.lower()
        if material == "shards" or material == "fragments" or material == "motes":
            winners[material] += quant
            if winners["shards"] or winners["fragments"] or winners["motes"] >= 250:
                if winners.get("shards") >= 250:
                    item = "Shadowmourne"
                    winners["shards"] -= 250
                    break
                elif winners.get("fragments") >= 250:
                    item = "Valanyr"
                    winners["fragments"] -= 250
                    break
                elif winners.get("motes") >= 250:
                    item = "Dragonwrath"
                    winners["motes"] -= 250
                    break
        else:
            if material not in dkt:
                dkt[material] = 0
            dkt[material] += int(quant)
print(item + " obtained!")
winners = dict(sorted(winners.items(), key=lambda x: (-x[1], x[0])))
dkt = dict(sorted(dkt.items(), key=lambda x1: (x1[0], -x1[1])))
for key, value in winners.items():
    print(f"{key}: {value}")
for key, value in dkt.items():
    print(f"{key}: {value}")
