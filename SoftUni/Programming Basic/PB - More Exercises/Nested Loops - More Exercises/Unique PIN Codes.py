first_number = int(input())
second_number = int(input())
third_number = int(input())

for a in range(1, first_number + 1):
    if second_number > 7:
        second_number = 7
    for b in range(2, second_number + 1):
        is_prime = True
        for d in range(2, b):
            if b % d == 0:
                is_prime = False
        for c in range(1, third_number + 1):
            if a % 2 == 0 and c % 2 == 0 and is_prime:
                print(f'{a} {b} {c}')
