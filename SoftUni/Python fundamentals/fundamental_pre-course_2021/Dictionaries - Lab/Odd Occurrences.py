lst = input().split(' ')
dkt = {}
for i in lst:
    i_lower = i.lower()
    if i_lower not in dkt:
        dkt[i_lower] = 0
    dkt[i_lower] += 1
for key, value in dkt.items():
    if not value % 2 == 0:
        print(key, end=' ')
