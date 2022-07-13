data = input()
dkt = {}
while not data == "no more time":
    name, contest, points = data.split(" -> ")
    points = int(points)
    if contest not in dkt:
        dkt[contest] = {}
    if name not in dkt[contest]:
        dkt[contest][name] = points
    else:
        if dkt[contest][name] <= points:
            dkt[contest][name] = points
    data = input()

for i, s in dkt.items():
    sorted_dkt = dict(sorted(s.items(), key=lambda x: (-x[1], x[0])))
    count_people = len(sorted_dkt)
    print(f"{i}: {count_people} participants")
    flag = 0
    for k, v in sorted_dkt.items():
        flag += 1
        print(f"{flag}. {k} <::> {v}")

sum_dict = {}
for a, b in dkt.items():
    for c, d in b.items():
        if c not in sum_dict:
            sum_dict[c] = d
        else:
            sum_dict[c] += d

sum_dict = dict(sorted(sum_dict.items(), key=lambda x: (-x[1], x[0])))
print("Individual standings:")
counter = 1
for y, z in sum_dict.items():
    print(f"{counter}. {y} -> {z}")
    counter += 1
