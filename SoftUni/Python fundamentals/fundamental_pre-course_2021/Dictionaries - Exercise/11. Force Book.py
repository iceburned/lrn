dkt = {}
data = input()
while not data == "Lumpawaroo":
    if "|" in data:
        force_side, force_user = data.split(" | ")
        if force_side not in dkt:
            dkt[force_side] = []
        if force_user not in dkt.values():
            dkt[force_side].append(force_user)
    elif "->" in data:
        force_user, force_side = data.split(" -> ")
        for k, v in dkt:
            if force_user in v:
                print("ok")


    data = input()
