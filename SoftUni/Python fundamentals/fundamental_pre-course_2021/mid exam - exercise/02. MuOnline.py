lst = input().split("|")
health = 100
bitcoins = 0
room = 0
flag = True
for i in lst:
    room += 1
    item, points = i.split(' ')
    points = int(points)
    if item == 'potion':
        if health + points >= 100:
            points = 100 - health
            health = 100
        else:
            health += points
        print(f"You healed for {points} hp.")
        print(f"Current health: {health} hp.")
    elif item == 'chest':
        bitcoins += points
        print(f"You found {points} bitcoins.")
    else:
        health -= points
        if health > 0:
            print(f"You slayed {item}.")
        else:
            print(f"You died! Killed by {item}.")
            print(f"Best room: {room}")
            flag = False
            break
if flag:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
