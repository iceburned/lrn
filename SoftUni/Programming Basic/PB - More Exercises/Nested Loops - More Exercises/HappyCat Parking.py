days = int(input())
day_hours = int(input())

price_per_day = 0
price_sum = 0
for a in range(1, days + 1):
    for b in range(1, day_hours + 1):
        if a % 2 == 0 and b % 2 != 0:
            price_per_day += 2.50
            price_sum += 2.50
        elif a % 2 != 0 and b % 2 == 0:
            price_per_day += 1.25
            price_sum += 1.25
        else:
            price_per_day += 1
            price_sum += 1
    print(f"Day: {a} - {price_per_day:.2f} leva")
    price_per_day = 0
print(f"Total: {price_sum:.2f} leva")
