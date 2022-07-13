data = input()
dkt = {}
while not data == "end":
    language, name = data.split(" : ")
    if language not in dkt:
        dkt[language] = []
    dkt[language] += [name]
    data = input()
for key, values in dkt.items():
    print(f'{key}: {len(values)}')
    for i in values:
        print(f"-- {i}")
