rotation = int(input())
dkt = {}
dkt_average = {}
for _ in range(rotation):
    name = input()
    grade = float(input())
    if name not in dkt:
        dkt[name] = []
    dkt[name] += [grade]
for key, value in dkt.items():
    sum_sum = sum(value) / len(value)
    dkt_average[key] = sum_sum
dkt_average = dict(sorted(dkt_average.items(), key=lambda x: -x[1]))
for key, value in dkt_average.items():
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")
