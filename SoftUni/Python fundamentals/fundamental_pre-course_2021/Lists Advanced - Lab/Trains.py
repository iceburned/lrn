wagons = int(input())
lst = []
for i in range(wagons):
    lst.append(0)
param = ''
while not param == 'End':
    param = input()
    if 'add' in param:
        people = int(param.split()[1])
        lst_len = len(lst) - 1
        lst_last = lst[lst_len]
        lst.pop(lst_len)
        lst.append(lst_last + people)
    elif 'insert' in param:
        people1 = int(param.split()[2])
        wagon_count = int(param.split()[1])
        lst_last1 = lst[wagon_count]
        lst.pop(wagon_count)
        lst.insert(wagon_count, lst_last1 + people1)
    elif 'leave' in param:
        people2 = int(param.split()[2])
        wagon_count1 = int(param.split()[1])
        lst_last2 = lst[wagon_count1]
        lst.pop(wagon_count1)
        lst.insert(wagon_count1, lst_last2 - people2)
print(lst)
