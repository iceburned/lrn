num = int(input())

count = 0
count_memory = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if a * b + c * d == num:
                        count += 1
                        print(f'{a}{b}{c}{d}', end=' ')

                        if count == 4:
                            count_memory = str(a) + str(b) + str(c) + str(d)
print('')
if count >= 4:
    print(f'Password: {count_memory}')
else:
    print('No!')
