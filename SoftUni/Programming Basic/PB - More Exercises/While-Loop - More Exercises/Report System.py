total_sum = int(input())

count = 0
cash = 0
counter_cash = 0
card = 0
counter_card = 0
sum_sum = 0
while True:
    object_price = input()
    if object_price == "End":
        break
    object_price1 = int(object_price)  # обръщане в int
    count += 1
    if count % 2 != 0:  # за смяна карта/ в брой
        if object_price1 <= 100:
            counter_cash += 1
            cash += object_price1
            sum_sum = card + cash
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if object_price1 >= 10:
            card += object_price1
            counter_card += 1
            sum_sum = card + cash
            print("Product sold!")
        else:
            print("Error in transaction!")
    if total_sum <= sum_sum:
        break

if sum_sum >= total_sum:
    cash1 = cash / counter_cash
    card1 = card / counter_card
    print(f'Average CS: {cash1:.2f}\nAverage CC: {card1:.2f}')
else:
    print(f'Failed to collect required money for charity.')
