string_1, string_2 = input().split(" ")
lst1 = []
lst2 = []
lst_sum = []
for i in string_1:
    lst1.append(ord(i))
for s in string_2:
    lst2.append(ord(s))
if len(lst1) == len(lst2):
    for asd in range(len(lst1)):
        lst_sum.append(lst1[asd] * lst2[asd])
else:
    if len(lst1) < len(lst2):
        for asd in range(len(lst1)):
            lst_sum.append(lst1[asd] * lst2[asd])
        lst2 = lst2[len(lst1):]
        for i in lst2:
            lst_sum.append(i)
    elif len(lst1) > len(lst2):
        for asd in range(len(lst2)):
            lst_sum.append(lst1[asd] * lst2[asd])
        lst1 = lst1[len(lst2):]
        for i in lst1:
            lst_sum.append(i)
print(sum(lst_sum))
