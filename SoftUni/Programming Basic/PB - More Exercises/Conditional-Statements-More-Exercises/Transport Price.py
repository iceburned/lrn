kilometers = int(input())
day_night = input()

taxi = 0
bus = 0
train = 0

if day_night == "day":
    if kilometers < 20:
        taxi = (0.79 * kilometers) + 0.70
        print(f'{taxi:.2f}')
    elif 20 <= kilometers < 100:
        bus = 0.09 * kilometers
        print(f'{bus:.2f}')
    elif kilometers >= 100:
        bus = 0.09 * kilometers
        train = 0.06 * kilometers
        if bus <= train:
            print(f'{bus:.2f}')
        else:
            print(f'{train:.2f}')
    else:
        pass
elif day_night == "night":
    if kilometers < 20:
        taxi = (0.90 * kilometers) + 0.70
        print(f'{taxi:.2f}')
    elif 20 <= kilometers < 100:
        bus = 0.09 * kilometers
        print(f'{bus:.2f}')
    elif kilometers >= 100:
        bus = 0.09 * kilometers
        train = 0.06 * kilometers
        if bus <= train:
            print(f'{bus:.2f}')
        else:
            print(f'{train:.2f}')
    else:
        pass
else:
    pass
