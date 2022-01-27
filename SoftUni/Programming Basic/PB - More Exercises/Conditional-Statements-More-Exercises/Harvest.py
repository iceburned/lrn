import math

dekar_loze = int(input())
grozde_za_kvadrat = float(input())
needed_wine = int(input())
workers = int(input())

harvested_grapes = dekar_loze * grozde_za_kvadrat
wine = (harvested_grapes * 0.40) / 2.5

if wine >= needed_wine:
    wine1 = wine - needed_wine
    wine_per_person = wine1 / workers
    print(f'Good harvest this year! Total wine: {math.floor(wine)} liters.')
    print(f'{math.ceil(wine1)} liters left -> {math.ceil(wine_per_person)} liters per person.')
else:
    wine2 = needed_wine - wine
    print(f'It will be a tough winter! More {math.floor(wine2)} liters wine needed.')
