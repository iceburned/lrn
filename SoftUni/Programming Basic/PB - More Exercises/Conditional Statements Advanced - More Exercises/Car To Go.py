budget = float(input())
season = input()

type_car = ''
car = 0
class_car = ''
if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        car = budget * 0.35
        type_car = "Cabrio"
    elif season == "Winter":
        type_car = "Jeep"
        car = budget * 0.65
    else:
        pass
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        car = budget * 0.45
        type_car = "Cabrio"
    elif season == "Winter":
        type_car = "Jeep"
        car = budget * 0.80
    else:
        pass
elif budget > 500:
    class_car = "Luxury class"
    type_car = "Jeep"
    car = budget * 0.90
else:
    pass

print(class_car)
print(f'{type_car} - {car:.2f}')
