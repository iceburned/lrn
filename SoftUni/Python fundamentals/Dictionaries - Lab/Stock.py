lst = input().split(' ')
do_we_have = input().split(' ')
dkt = {}
for i in range(0, len(lst), 2):
    key = lst[i]
    value = lst[i + 1]
    dkt[key] = int(value)
for item in do_we_have:
    if item in dkt:
        print(f'We have {dkt.get(item)} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")
