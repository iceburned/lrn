import sys

str_input = input().split('|')
init_energy = 100
init_coins = 100
flag = False
for a in str_input:
    b = a.split('-')
    b1 = int(b[1])
    b2 = b[0]
    if flag:
        print(f'Closed! Cannot afford {b2}.')
        sys.exit()
    elif b2 == 'rest':
        if init_energy < 100:
            init_energy += b1
            print(f'You gained {b1} energy.')
            print(f'Current energy: {init_energy}.')
            continue
        else:
            init_energy = 100
            print(f'You gained {0} energy.\nCurrent energy: {init_energy}.')
            continue
    elif b2 == 'order':
        if init_energy >= 30:
            init_energy -= 30
            init_coins += b1
            print(f'You earned {b1} coins.')
            continue
        else:
            init_energy += 50
            print('You had to rest!')
            continue
    if init_coins >= 0 and init_coins >= b1:
        print(f'You bought {b2}.')
        init_coins -= b1
    else:
        flag = True
print(f'Day completed!\nCoins: {init_coins}\nEnergy: {init_energy}')
