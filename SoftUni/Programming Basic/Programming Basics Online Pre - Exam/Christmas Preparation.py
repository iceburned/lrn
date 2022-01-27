rolls_paper = int(input())
rolls_cloth = int(input())
glue_liters = float(input())
discount = int(input())

price_rolls_paper = rolls_paper * 5.80
price_rolls_cloth = rolls_cloth * 7.20
price_glue_liters = glue_liters * 1.20
price_sum = price_glue_liters + price_rolls_paper + price_rolls_cloth
discount1 = discount / 100
price_discount = price_sum - (price_sum * discount1)
print(f'{price_discount:.3f}')
