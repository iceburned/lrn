coin_one_lev = int(input())
coin_two_leva = int(input())
paper_five_leva = int(input())
sum_sum = int(input())

for a in range(0, coin_one_lev + 1):
    for b in range(0, coin_two_leva + 1):
        for c in range(0, paper_five_leva + 1):
            if (a * 1 + b * 2 + c * 5) == sum_sum:
                print(f'{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {sum_sum} lv.')
