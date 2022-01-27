sum_sum = 0
while sum_sum >= 0:
    single_sum = input()
    if single_sum == "NoMoreMoney":
        break
    elif float(single_sum) < 0:
        print('Invalid operation!')
        break
    sum_sum += float(single_sum)
    print(f'Increase: {float(single_sum):.2f}')
print(f'Total: {sum_sum:.2f}')
