lst = input().split()
item = ''
ite = ''
while ite != 'No Money':
    ite = input()
    item = ite.split()
    item0 = item[0]
    item1 = item[1]
    if item0 == 'OutOfStock':
        for a in lst:
            if a == item1:
                lst.remove(item1)
    elif item0 == 'Required':
        item2 = int(item[2]) - 1
        if item1 not in lst:
            lst[item2] = item1
    elif item0 == 'JustInCase':
        lst.pop()
        lst.append(item1)
for b in lst:
    print(b, end=' ')






