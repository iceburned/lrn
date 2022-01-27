moves = int(input())

num = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
unvalid = 0

sum_sum = 0
for _ in range(moves):
    single_move = int(input())
    if 0 <= single_move <= 9:
        num += single_move * 0.2
        sum_sum += single_move
    elif 10 <= single_move <= 19:
        num1 += single_move * 0.3
        sum_sum += single_move
    elif 20 <= single_move <= 29:
        num2 += single_move * 0.4
        sum_sum += single_move
    elif 30 <= single_move <= 39:
        num3 += 50
        sum_sum += single_move
    elif 40 <= single_move <= 50:
        num4 += 100
        sum_sum += single_move
    elif -1 <= single_move or single_move > 50:
        unvalid += single_move

unvalid1 = unvalid / 2
print(sum_sum)
