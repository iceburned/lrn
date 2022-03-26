data = input()
dkt = {}
count = {}
while not data == "exam finished":
    if "banned" not in data:
        name, lang, points = data.split("-")
        points = int(points)
        if lang not in count:
            count.update({lang: 1})
        else:
            count[lang] += 1
        if name not in dkt:
            dkt.update({name: {}})
        if lang not in dkt[name]:
            dkt[name].update({lang: 0})
        if dkt[name][lang] < points:
            dkt[name][lang] = points
    else:
        person, command = data.split("-")
        dkt.pop(person)
    data = input()
print("Results:")
for k, v in dkt.items():
    for s in v:
        print(f"{k} | {v[s]}")
print("Submissions:")
for a in count:
    print(f"{a} - {count[a]}")
