s1 = str(input())
s2 = str(input())
list1 = list(s1.strip())
list2 = list(s2.strip())

for i in range(len(s1)):
    if list1[i] == list2[i]:
        continue
    else:
        list1[i] = list2[i]
    print(''.join(list1))
