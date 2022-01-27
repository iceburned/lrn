stay_days = int(input()) - 1
room = input()
pos_or_neg = input()

sum_sum = 0


if room == "room for one person":
    sum_sum = stay_days * 18.00

elif room == "apartment":
    sum_sum = stay_days * 25.00
    if stay_days < 10:
        sum_sum -= sum_sum * 0.30
    elif 10 < stay_days < 15:
        sum_sum -= sum_sum * 0.35
    else:
        sum_sum -= sum_sum * 0.50

elif room == "president apartment":
    sum_sum = stay_days * 35.00
    if stay_days < 10:
        sum_sum -= sum_sum * 0.10
    elif 10 < stay_days < 15:
        sum_sum -= sum_sum * 0.15
    else:
        sum_sum -= sum_sum * 0.20

if pos_or_neg == "positive":
    sum_sum += sum_sum * 0.25
else:
    sum_sum -= sum_sum * 0.10

print(f'{sum_sum:.2f}')
