lst = input().split()
item = ''
ite = input()
while ite != 'No Money':
    item = ite.split()
    item0 = item[0]
    item1 = item[1]
    if item0 == 'OutOfStock':
        for a in range(len(lst)):
            if lst[a] == item1:
                lst[a] = 'None'
    elif item0 == 'Required':
        item2 = int(item[2])
        if len(lst) > item2 >= 0:
            if item1 not in lst:
                lst[item2] = item1
    elif item0 == 'JustInCase':
        lst.pop()
        lst.append(item1)
    ite = input()
# for b in lst:
#     if not b == 'None':
#         print(b, end=' ')
print(*[_ for _ in lst if not _ == 'None'], end=' ')
