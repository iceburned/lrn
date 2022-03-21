def plunder(my_dict, tow, peop, gol):
    peop = int(peop)
    gol = int(gol)
    my_dict[tow]["population"] -= peop
    my_dict[tow]["gold"] -= gol
    if my_dict[tow]["population"] <= 0 or my_dict[tow]["gold"] <= 0:
        my_dict.pop(tow)
        print(f"{tow} plundered! {gol} gold stolen, {peop} citizens killed.")
        print(f"{tow} has been wiped off the map!")
    else:
        print(f"{tow} plundered! {gol} gold stolen, {peop} citizens killed.")
    return my_dict


def prosper(my_dict, tow, gol):
    gol =int(gol)
    if gol < 0:
        print("Gold added cannot be a negative number!")
        return my_dict
    else:
        my_dict[tow]["gold"] += gol
        print(f"{gol} gold added to the city treasury. {tow} now has {my_dict[tow]['gold']} gold.")
        return my_dict


cities = {}
cities_input = input()
while not cities_input == "Sail":
    town, population, gold = cities_input.split("||")
    population = int(population)
    gold = int(gold)
    if town not in cities:
        cities.update({town: {"population": 0, "gold": 0}})
    cities[town]["population"] += population
    cities[town]["gold"] += gold
    cities_input = input()
cities_action = input()
while not cities_action == "End":
    if cities_action.startswith("Plunder"):
        comm, town, people, gold = cities_action.split("=>")
        cities = plunder(cities, town, people, gold)
    elif cities_action.startswith("Prosper"):
        comm, town, gold = cities_action.split("=>")
        cities = prosper(cities, town, gold)
    cities_action = input()
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for i in cities:
        print(f"{i} -> Population: {cities[i]['population']} citizens, Gold: {cities[i]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
