import math

needed_hours = int(input())
days = int(input())
workers = int(input())

days_train = days * 0.90
sum_hours = days_train * 8
workers_hours = workers * 2 * days

sum_sum = math.floor(sum_hours + workers_hours)
s = abs(sum_sum - needed_hours)

if sum_sum >= needed_hours:
    print(f'Yes!{math.floor(s)} hours left.')
else:
    print(f'Not enough time!{math.floor(s)} hours needed.')
