import math

days = int(input())
food_by_kg = int(input())
dog_food = float(input())
cat_food = float(input())
turt_food = float(input())

dog_food1 = days * dog_food
cat_food1 = days * cat_food
turt_food1 = (days * turt_food) / 1000

sum_food = dog_food1 + cat_food1 + turt_food1

if sum_food <= food_by_kg:
    s = food_by_kg - sum_food
    print(f'{math.floor(s)} kilos of food left.')
else:
    s = sum_food - food_by_kg
    print(f'{math.ceil(s)} more kilos of food are needed.')
