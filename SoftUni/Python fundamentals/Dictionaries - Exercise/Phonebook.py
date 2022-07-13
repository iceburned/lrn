data = input()
dkt = {}
while not len(data) < 2:
    key, value = data.split('-')
    dkt[key] = value
    data = input()
for i in range(int(data)):
    name = input()
    if name in dkt:
        print(f"{name} -> {dkt[name]}")
    else:
        print(f"Contact {name} does not exist.")
