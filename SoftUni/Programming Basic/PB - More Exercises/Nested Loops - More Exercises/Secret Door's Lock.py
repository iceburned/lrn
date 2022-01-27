upper_digit = int(input())
middle_digit = int(input())
lower_digit = int(input())

for a in range(1, upper_digit + 1):
    if a % 2 == 0:
        for b in range(2, middle_digit + 1):
            is_prime = True
            for d in range(2, b):
                if b % d == 0:
                    is_prime = False
            for c in range(1, lower_digit + 1):
                if c % 2 == 0 and is_prime:
                    print(f'{a} {b} {c}')
