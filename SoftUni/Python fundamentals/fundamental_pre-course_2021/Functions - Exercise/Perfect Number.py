def perf_num(num):
    sum_sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum_sum += i
    if sum_sum == num:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


print(perf_num(int(input())))
