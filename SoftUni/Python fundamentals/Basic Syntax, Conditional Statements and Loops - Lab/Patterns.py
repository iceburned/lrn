num = int(input())

for a in range(1, num + 1):
    for b in range(1, a + 1):
        print('*', end='')
    print('')
for a in range(num, 1, -1):
    for b in range(a, 1, -1):
        print('*', end='')
    print('')
