# lst = []
# input_data = input()
# while not input_data == 'End':
#     lst_add = lst.append(input_data)
#     lst.sort()
#     input_data = input()
# for i in range(len(lst)):
#     data = lst[i]
#     data1 = data[2:]
#     lst.pop(i)
#     lst.insert(i, data1)
# print(lst)
lst = [0] * 10
input_data = input()
while not input_data == 'End':
    a = input_data.split("-")
    lst.pop(int(a[0])-1)
    lst.insert(int(a[0])-1, a[1])
    input_data = input()
# [lst.remove(0) for _ in lst]
for i in range(len(lst)):
    if 0 in lst:
        lst.remove(0)
print(lst)
