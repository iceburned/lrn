dkt = {}
data = input()
while not data == "Lumpawaroo":
    if "|" in data:
        force_side, force_user = data.split(" | ")
        if force_side not in dkt and force_user not in dkt:
            dkt[force_side] = []
        if force_user not in dkt.values():
            dkt[force_side].append(force_user)
    elif "->" in data:
        force_user, force_side = data.split(" -> ")
        if force_side not in dkt:
            dkt[force_side] = []
        if force_user not in dkt[force_side] and [True for _ in dkt.values() if force_user in _]:
            i = ''
            for i in dkt:
                if force_user in dkt[i]:
                    a = 2
                    dkt[i].remove(force_user)
            if not dkt[i]:
                dkt.pop(i)
            dkt[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        else:
            if force_user not in dkt.values():
                dkt[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
    data = input()
for a, b in dkt.items():
    count_sum = len(b)
    print(f"Side: {a}, Members: {count_sum}")
    for s in b:
        print(f"! {s}")
