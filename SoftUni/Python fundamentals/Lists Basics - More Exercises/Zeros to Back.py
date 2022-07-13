lst = input().split(',')
lst = [int(_) for _ in lst]
for a in lst:
    if a == 0:
        lst.remove(0)
        lst.append(a)
print(lst)
