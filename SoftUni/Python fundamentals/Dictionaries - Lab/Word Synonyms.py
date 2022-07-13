num = int(input())
dkt = {}
for i in range(num):
    key = input()
    value = input()
    if key in dkt:
        dkt[key].append(value)
    else:
        dkt[key] = []
        dkt[key].append(value)
for a in dkt:
    print(f'{a} - {", ".join(dkt[a])}')

# drug variant
# for key, value in dkt.items():
#     print(f'{key} - {", ".join(value)}')