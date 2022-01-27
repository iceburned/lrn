days = int(input())

drink = 0
celsius = 0

for _ in range(1, days + 1):
    drink_liters = float(input())
    celsius_drink = float(input())
    drink += drink_liters
    celsius += drink_liters * celsius_drink

celsius_sum = celsius / drink
print(f'Liter: {drink:.2f}\nDegrees: {celsius_sum:.2f}')
if celsius_sum < 38:
    print('Not good, you should baking!')
elif 38 <= celsius_sum <= 42:
    print('Super!')
elif celsius_sum > 42:
    print('Dilution with distilled water!')
