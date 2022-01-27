budget = float(input())
product = input()
count_product = 0
count_price = 0
while True:
    if product == "Stop":
        print(f"You bought {count_product} products for {count_price:.2f} leva.")
        break
    price_product = float(input())
    if (budget - price_product) < 0:
        print("You don't have enough money!")
        print(f"You need {abs(budget - price_product):.2f} leva!")
        break
    count_product += 1
    if count_product % 3 == 0:
        price_product = price_product / 2
    budget -= price_product
    count_price += price_product
    product = input()
