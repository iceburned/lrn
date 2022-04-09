dkt = {}
data = [_ for _ in input()]
for s in data:
    num = data.count(s)
    dkt.update({s: num})
dkt = dict(sorted(dkt.items(), key=lambda x: x[0]))
[print(f"{k}: {dkt[k]} time/s") for k in dkt]
