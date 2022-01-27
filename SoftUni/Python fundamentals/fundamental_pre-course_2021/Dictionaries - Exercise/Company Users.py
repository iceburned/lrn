data = input()
dkt = {}
while not data == 'End':
    key, value = data.split(" -> ")
    flag = False
    if key not in dkt:
        dkt[key] = []
    for i in dkt[key]:
        if value in i:
            flag = True
    if not flag:
        dkt[key] += [value]
    data = input()
'''В условието пише да се сортира, обаче  в Judge трябва да е без сортировка'''
# dkt = dict(sorted(dkt.items(), key=lambda x: x, reverse=True))
for a in dkt.keys():
    print(a)
    for b in dkt[a]:
        print(f"-- {''.join(b)}")
