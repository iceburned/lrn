young = int(input())
oldest = int(input())
type_trace = input()


juniors = 0
seniors = 0
if type_trace == "trail":
    juniors = 5.50
    seniors = 7
elif type_trace == "cross-country":
    juniors = 8
    seniors = 9.50
elif type_trace == "downhill":
    juniors = 12.25
    seniors = 13.75
elif type_trace == "road":
    juniors = 20
    seniors = 21.50
else:
    pass

sum_sum = juniors * young + seniors * oldest
count_people = young + oldest
if type_trace == "cross-country" and count_people >= 50:
    sum_sum -= sum_sum * 0.25
else:
    pass

sum_sum -= sum_sum * 0.05

print(f'{sum_sum:.2f}')
