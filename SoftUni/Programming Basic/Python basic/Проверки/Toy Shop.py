holiday = float(input())
puzzle = int(input())
talking_doll = int(input())
taddy_bear = int(input())
minions = int(input())
trucks = int(input())

total = (puzzle * 2.60) + (talking_doll * 3) + (taddy_bear * 4.10) + (minions * 8.20) + (trucks * 2)
toys_sum = puzzle + talking_doll + taddy_bear + minions + trucks
if toys_sum >= 50:
    total -= total * 0.25
# Rent
total -= total * 0.10
# holiday
total -= holiday
if total >= 0:
    print(f"Yes! {total:.2f} lv left.")
else:
    print(f"Not enough money! {abs(total):.2f} lv needed.")
