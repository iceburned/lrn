fuel_type = input()
quantity_fuel = int(input())
club_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93

if club_card == "Yes":
    gasoline -= 0.18
    diesel -= 0.12
    gas -= 0.08
else:
    pass

gasoline1 = gasoline * quantity_fuel
diesel1 = diesel * quantity_fuel
gas1 = gas * quantity_fuel

# if 20 <= gasoline <= 25 or 20 <= diesel <= 25 or 20 <= gas <= 25:
if 20 <= quantity_fuel <= 25:
    gasoline1 -= gasoline1 * 0.08
    diesel1 -= diesel1 * 0.08
    gas1 -= gas1 * 0.08
elif 19 >= gasoline1 or 19 >= diesel1 or 19 >= gas1:
    pass
else:
    gasoline1 -= gasoline1 * 0.10
    diesel1 -= diesel1 * 0.10
    gas1 -= gas1 * 0.10

if fuel_type == "Gasoline":
    print(f'{gasoline1:.2f} lv.')
elif fuel_type == "Diesel":
    print(f'{diesel1:.2f} lv.')
elif fuel_type == "Gas":
    print(f'{gas1:.2f} lv.')
else:
    pass
