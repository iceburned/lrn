generator = int(input())
data = input()
dkt = {}

for i in range(generator):
    plant, rarity = data.split("<->")
    dkt.update({plant: {"rarity": int(rarity), "rating": []}})
    data = input()


while not data == "Exhibition":
    comm, action = data.split(": ")
    if comm.startswith("Rate"):
        name, num = action.split(" - ")
        num = int(num)
        if name in dkt:
            dkt[name]["rating"].append(num)
        else:
            print("error")
    elif comm.startswith("Update"):
        name, num = action.split(" - ")
        num = int(num)
        if name in dkt:
            dkt[name]["rarity"] = num
        else:
            print("error")
    elif comm.startswith("Reset"):
        if action in dkt:
            dkt[action]["rating"].clear()
            # dkt[action]["rating"].append(0)
        else:
            print("error")
    data = input()
print("Plants for the exhibition:")
for k, v in dkt.items():
    rar = v["rarity"]
    rat = v["rating"]
    avg = 0
    if rat:
        avg = sum(rat) / len(rat)
    print(f"- {k}; Rarity: {rar}; Rating: {avg:.2f}")