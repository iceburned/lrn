import math
group_size = int(input())
days = int(input())
sum_sum = 0
flag = False
for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
    sum_sum += 50
    party_expenses = group_size * 2
    sum_sum -= party_expenses
    if i % 3 == 0:
        sum_sum -= group_size * 3
        flag = True
    if i % 5 == 0:
        sum_sum += group_size * 20
        if flag:
            sum_sum -= group_size * 2
    flag = False
print(f"{group_size} companions received {math.floor(sum_sum / group_size)} coins each.")
