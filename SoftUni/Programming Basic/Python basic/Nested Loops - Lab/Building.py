floor = int(input())
apartment = int(input())

for f in range(floor, 0, -1):
    for a in range(0, apartment):
        if floor == f:
            print('L' + str(f) + str(a), end=' ')
        elif f % 2 == 0:
            print('O' + str(f) + str(a), end=' ')
        else:
            print('A' + str(f) + str(a), end=' ')

    print('')
