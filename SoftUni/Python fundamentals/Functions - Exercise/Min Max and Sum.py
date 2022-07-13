def min_max_sum(strin_num):
    strin_num = [int(_) for _ in strin_num]
    num_min = min(strin_num)
    num_max = max(strin_num)
    num_sum = sum(strin_num)
    return f'The minimum number is {num_min}\nThe maximum number is {num_max}' \
           f'\nThe sum number is: {num_sum}'


print(min_max_sum(input().split()))
