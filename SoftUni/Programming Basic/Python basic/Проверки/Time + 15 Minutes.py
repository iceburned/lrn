hour = int(input())
min1 = int(input())

min1 += 15
if min1 > 59:
    hour += 1
    min1 = min1 % 60
if hour > 23:
    hour = 0
if min1 == 60:
    min1 = 0
if min1 < 10:
    print(f'{hour}:0{min1}')
else:
    print(f'{hour}:{min1}')
