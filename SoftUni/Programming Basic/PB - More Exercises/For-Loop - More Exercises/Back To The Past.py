money = float(input())
years_life = int(input())
money1 = money
years = 17
for _ in range(1800, years_life + 1):
    if _ % 2 == 0:
        money1 -= 12000
        years += 1
    else:
        years += 1
        money1 -= 12000 + (50 * years)
if money >= money1 >= 0:
    print(f"Yes! He will live a carefree life and will have {money1:.2f} dollars left.")
else:
    print(f"He will need {abs(money1):.2f} dollars to survive.")
