num = float(input())

if num == 0:
    print('zero')
elif num < 0:
    if 0 > num > -1:
        print('small negative')
    elif -1 > num > -1000000:
        print('negative')
    else:
        print('large negative')
elif num > 0:
    if 0 < num < 1:
        print('small positive')
    elif 1 < num < 1000000:
        print('positive')
    else:
        print('large positive')
