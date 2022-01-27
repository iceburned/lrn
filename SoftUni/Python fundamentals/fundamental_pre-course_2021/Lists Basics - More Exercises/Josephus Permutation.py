lst = input().split()
lst = [int(_) for _ in lst]
num = int(input())
i = 0
lst1 = []
while lst:
    for a in range(len(lst)):
        i += 1
        if i == num:
            i = 0
            lst1.append(lst[a])
    for b in lst1:
        if b in lst:
            lst.remove(b)
lst1 = [str(_) for _ in lst1]
lst2 = ','.join(lst1)
print(f'[{lst2}]')
