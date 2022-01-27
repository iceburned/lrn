budget = float(input())
workers = int(input())
cloth_price = float(input())
decor = budget * 0.10
cloth = workers * cloth_price
cloth_bonus = 0
if workers > 150:
    cloth_bonus = cloth * 0.10
cloth1 = cloth - cloth_bonus
sum_sum = budget - (cloth1 + decor)
if sum_sum >= 0:
    print(f'Action! \nWingard starts filming with {sum_sum:.2f} leva left.')
else:
    print(f'Not enough money! \nWingard needs {abs(sum_sum):.2f} leva more.')
