num = int(input())
total_price = 0
for i in range(num):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    sum_sum = price_per_capsule * days * capsule_count
    total_price += sum_sum
    print(f'The price for the coffee is: ${sum_sum:.2f}')
print(f'Total: ${total_price:.2f}')
