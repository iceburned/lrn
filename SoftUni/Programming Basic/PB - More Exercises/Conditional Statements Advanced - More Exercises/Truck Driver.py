season = input()
km_per_month = float(input())

km_sum = 0
if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        km_sum = km_per_month * 0.75
    elif season == "Summer":
        km_sum = km_per_month * 0.90
    elif season == "Winter":
        km_sum = km_per_month * 1.05
elif 5000 <= km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        km_sum = km_per_month * 0.95
    elif season == "Summer":
        km_sum = km_per_month * 1.10
    elif season == "Winter":
        km_sum = km_per_month * 1.25
elif km_per_month > 10000:
    km_sum = km_per_month * 1.45
else:
    pass
km_sum1 = km_sum - (km_sum * 0.10)
km_sum2 = km_sum1 * 4
print(f'{km_sum2:.2f}')
