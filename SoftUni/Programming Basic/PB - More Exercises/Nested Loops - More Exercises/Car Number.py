first_number = int(input())
second_number = int(input())

for a in range(first_number, second_number + 1):
    for b in range(first_number, second_number + 1):
        for c in range(first_number, second_number + 1):
            for d in range(first_number, second_number + 1):
                if (a % 2 == 0 and d % 2 != 0) or (a % 2 != 0 and d % 2 == 0):
                    if a > d and (b + c) % 2 == 0:
                        print(f'{a}{b}{c}{d}', end=' ')
