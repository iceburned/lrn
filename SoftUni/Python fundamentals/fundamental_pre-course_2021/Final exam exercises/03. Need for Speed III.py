def drive(autos, auto, dist, fuell):
    autos[auto]["milage"] += dist
    autos[auto]["fuel"] -= fuell
    if autos[auto]["milage"] >= 100000:
        print(f"{auto} driven for {dist} kilometers. {fuell} liters of fuel consumed.")
        print(f"Time to sell the {auto}!")
        autos.pop(auto)
    else:
        print(f"{auto} driven for {dist} kilometers. {fuell} liters of fuel consumed.")
    return autos

def refuel(autos, auto, fuell):
    fuel_momentum = autos[auto]["fuel"]
    if fuel_momentum + fuell >= 75:
        fuel_momentum = 75 - fuel_momentum
        autos[auto]["fuel"] = 75
    else:
        fuel_momentum = fuell
        autos[auto]["fuel"] += fuell
    print(f"{auto} refueled with {fuel_momentum} liters")
    return autos

def revert(autos, auto, km):
    autos[auto]["milage"] -= km
    momentum_km = 0
    if autos[auto]["milage"] <= 10000:
        momentum_km = 10000 - autos[auto]["milage"]
        autos[auto]["milage"] = 10000
    else:
        momentum_km = km
        print(f"{auto} mileage decreased by {momentum_km} kilometers")
    return autos


number_of_cars = int(input())
cars = {}
for i in range(number_of_cars):
    data = input().split("|")
    num = int(data[2])
    length = int(data[1])
    cars.update({data[0]: {"milage": length, "fuel": num}})
command = input()
while not command == "Stop":
    if command.startswith("Drive"):
        com, car, distance, fuel = command.split(" : ")
        fuel = int(fuel)
        distance = int(distance)
        if cars[car]["fuel"] >= fuel:
            cars = drive(cars, car, distance, fuel)
        else:
            print("Not enough fuel to make that ride")
    elif command.startswith("Refuel"):
        comm, car, fuel = command.split(" : ")
        fuel = int(fuel)
        cars = refuel(cars, car, fuel)
    elif command.startswith("Revert"):
        comm, car, kilometers = command.split(" : ")
        kilometers = int(kilometers)
        cars = revert(cars, car, kilometers)
    command = input()
for ss in cars:
    print(f"{ss} -> Mileage: {cars[ss]['milage']} kms, Fuel in the tank: {cars[ss]['fuel']} lt.")

