lst = input().split()
dkt = {}
for a in lst:
    for b in a:
        if b not in dkt:
            dkt[b] = 0
        dkt[b] += 1
for key, value in dkt.items():
    print(key + ' ->', value)
