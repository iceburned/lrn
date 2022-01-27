letters = input()
num = int(input())
lst = letters.split()
lst_sum = []
for b in range(num):
    len_half = len(lst) // 2
    str_1 = lst[:len_half]
    str_2 = lst[len_half:]
    for a in range(len(str_1)):
        lst_sum.append(str_1[a])
        lst_sum.append(str_2[a])
    lst = lst_sum
    lst_sum = []
print(lst)
