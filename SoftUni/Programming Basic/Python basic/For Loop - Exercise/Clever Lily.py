age = int(input())
wash_machine = float(input())
toy_single_price = int(input())

odd_toy = 0
even_money = 0
brother_money = 0
even_money1 = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        even_money += 10
        brother_money += 1
        even_money1 += even_money
    else:
        odd_toy += 1

toy_money = odd_toy * toy_single_price
sum_sum = even_money1 + toy_money - brother_money
if sum_sum >= wash_machine:
    sum_sum1 = sum_sum - wash_machine
    print(f'Yes! {sum_sum1:.2f}')
else:
    sum_sum2 = wash_machine - sum_sum
    print(f'No! {sum_sum2:.2f}')
