import math

magnolii = int(input())
ziumbiuli = int(input())
rozi = int(input())
cactus = int(input())
present = float(input())

sum_sum = magnolii * 3.25 + ziumbiuli * 4 + rozi * 3.50 + cactus * 8
sum_sum1 = sum_sum - (sum_sum * 0.05)
s = abs(present - sum_sum1)

if present >= sum_sum:
    print(f'She will have to borrow {math.ceil(s)} leva.')
else:
    print(f'She is left with {math.floor(s)} leva.')
