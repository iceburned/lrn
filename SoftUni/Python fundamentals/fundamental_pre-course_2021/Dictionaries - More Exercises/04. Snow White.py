dkt = {}
data = input()
while not data == "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = data.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    if dwarf_hat_color not in dkt:
        dkt[dwarf_hat_color] = {}
    if dwarf_hat_color in dkt and dwarf_name not in dkt[dwarf_hat_color]:
        dkt[dwarf_hat_color][dwarf_name] = dwarf_physics
    elif dwarf_name in dkt[dwarf_hat_color] and dkt[dwarf_hat_color][dwarf_name] < dwarf_physics:
        dkt[dwarf_hat_color][dwarf_name] = dwarf_physics
    data = input()

dkt = [(c, n, p, len(items)) for c, items in dkt.items() for n, p in items.items()]
for i in sorted(dkt, key=lambda x: (-x[2], -x[3])):
    c, n, p, _ = i
    print(f"({c}) {n} <-> {p}")
