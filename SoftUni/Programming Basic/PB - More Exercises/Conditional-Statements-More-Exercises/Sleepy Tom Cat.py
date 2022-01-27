count_rest_days = int(input())

rest_days_min = count_rest_days * 127
working_days_min = (365 - count_rest_days) * 63
sum_sum = rest_days_min + working_days_min
sum_sum4 = abs(30000 - sum_sum)
sum_sum1 = sum_sum4 // 60
sum_sum2 = sum_sum4 % 60

if 30000 >= sum_sum:

    print("Tom sleeps well")
    print(f"{sum_sum1} hours and {sum_sum2} minutes less for play")
else:
    print("Tom will run away")
    print(f"{sum_sum1} hours and {sum_sum2} minutes more for play")
