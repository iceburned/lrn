res_ource = input()
dkt = {}
while not res_ource == "stop":
    quantity = int(input())
    if res_ource not in dkt:
        dkt[res_ource] = 0
    dkt[res_ource] += quantity
    res_ource = input()
for key, value in dkt.items():
    print(key + ' -> ' + str(value))
