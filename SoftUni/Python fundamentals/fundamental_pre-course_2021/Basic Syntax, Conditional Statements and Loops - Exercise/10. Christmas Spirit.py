quantity = int(input())
days = int(input())
sum_sum = 0
spirits = 0
flag = False
for i in range(1, days + 1):
    if i % 2 == 0:
        sum_sum += quantity * 2
        spirits += 5
    if i % 3 == 0:
        sum_sum += quantity * 5
        sum_sum += quantity * 3
        spirits += 13
        flag = True
    if i % 5 == 0:
        sum_sum += quantity * 15
        spirits += 17
        if flag:
            spirits += 30
    if i % 10 == 0:
        spirits -= 20
        sum_sum += 23
    if i % 11 == 0:
        quantity += 2
    flag = False
if days % 10 == 0:
    spirits -= 30
print(f'Total cost: {sum_sum}\nTotal spirit: {spirits}')
