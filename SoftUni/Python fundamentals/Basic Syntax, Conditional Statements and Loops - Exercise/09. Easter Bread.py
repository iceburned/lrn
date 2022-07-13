budget = float(input())
price_for_kilo = float(input())
pack_eggs = price_for_kilo * 0.75
litre_milk = (price_for_kilo * 1.25)/4
one_brad = price_for_kilo + pack_eggs + litre_milk
sum_sum = 0
bread = 0
color_eggs = 0
while sum_sum <= budget and (one_brad + sum_sum) <= budget:
    color_eggs += 3
    bread += 1
    if bread % 3 == 0:
        color_eggs -= (bread - 2)
    sum_sum += price_for_kilo + pack_eggs + litre_milk
print(f'You made {bread} loaves of Easter bread! Now you have '
      f'{color_eggs} eggs and {(budget - sum_sum):.2f}BGN left.')
