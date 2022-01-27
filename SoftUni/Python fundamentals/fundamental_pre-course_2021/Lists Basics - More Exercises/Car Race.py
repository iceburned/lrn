lst = input().split()
lst = [int(_) for _ in lst]
lst_len = len(lst) // 2
first_lst = lst[:lst_len]
second_list = lst[lst_len + 1:]
second_list.reverse()
sum_sum1 = 0
sum_sum2 = 0
for s in first_lst:
    if s == 0:
        sum_sum1 = sum_sum1 - (sum_sum1 * 0.2)
    else:
        sum_sum1 += s
for f in second_list:
    if f == 0:
        sum_sum2 = sum_sum2 - (sum_sum2 * 0.2)
    else:
        sum_sum2 += f
if sum_sum1 <= sum_sum2:
    print(f'The winner is left with total time: {sum_sum1:.1f}')
else:
    print(f'The winner is right with total time: {sum_sum2:.1f}')
