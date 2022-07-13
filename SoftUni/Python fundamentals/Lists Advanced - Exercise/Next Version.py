import sys
lst = input().split('.')
lst = [int(_) for _ in lst]
first, second, third = lst
if not third == 9:
    third += 1
    print(f'{first}.{second}.{third}')
    sys.exit()
else:
    third = 0
    if not second == 9:
        second += 1
        print(f'{first}.{second}.{third}')
        sys.exit()
    else:
        second = 0
    if not first == 9:
        first += 1
        print(f'{first}.{second}.{third}')
        sys.exit()
