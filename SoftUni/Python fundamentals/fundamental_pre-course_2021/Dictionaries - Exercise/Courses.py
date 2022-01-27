data = input()
dkt = {}
while not data == "end":
    language, name = data.split(" : ")
    if language not in dkt:
        dkt[language] = []
    dkt[language] += [name]
    data = input()
dkt = dict(sorted(dkt.items(), key=lambda x: (len(x[1])), reverse=True))
for i in dkt.items():
    i[1].sort()
for key, values in dkt.items():
    print(f'{key}: {len(values)}')
    for i in values:
        print(f"-- {i}")
