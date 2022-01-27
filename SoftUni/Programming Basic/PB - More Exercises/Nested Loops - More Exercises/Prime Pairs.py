first_couple_lower_limit = int(input())  # 10/90
second_couple_lower_limit = int(input())  # 10/90
first_couple_min_max_difference = int(input())  # 1/9
second_couple_min_max_difference = int(input())  # 1/9

for first in range(first_couple_lower_limit, first_couple_lower_limit + first_couple_min_max_difference + 1):
    first_is_prime = True
    for i in range(2, 10):
        if first != i and first % i == 0:
            first_is_prime = False
            break
    if not first_is_prime:
        continue
    for second in range(second_couple_lower_limit, second_couple_lower_limit + second_couple_min_max_difference + 1):
        second_is_prime = True
        for i in range(2, 10):
            if second != i and second % i == 0:
                second_is_prime = False
                break
        if not second_is_prime:
            continue
        print(f"{first}{second}")
