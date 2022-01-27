cargo_count = int(input())

tons = 0
bus = 0
bus1 = 0
truck = 0
truck1 = 0
train = 0
train1 = 0
for _ in range(cargo_count):
    single_cargo = int(input())
    if single_cargo <= 3:
        bus += single_cargo * 200
        bus1 += single_cargo
        tons += single_cargo
    elif 4 <= single_cargo <= 11:
        truck += single_cargo * 175
        truck1 += single_cargo
        tons += single_cargo
    elif 12 <= single_cargo:
        train += single_cargo * 120
        train1 += single_cargo
        tons += single_cargo

average_tonnage = (bus + train + truck) / tons
sum_tonage = bus1 + truck1 + train1
average_bus = (bus1 / sum_tonage) * 100
average_truck = (truck1 / sum_tonage) * 100
average_train = (train1 / sum_tonage) * 100

print(f'{average_tonnage:.2f}\n{average_bus:.2f}%\n{average_truck:.2f}%\n{average_train:.2f}%')
