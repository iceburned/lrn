steps_sum = 0
while True:
    if steps_sum > 10000:
        break
    steps = input()

    if steps == 'Going home':
        steps_sum += int(input())
        break

    if steps_sum <= 10000:
        steps_sum += int(steps)

sum_sum = abs(10000 - steps_sum)
if steps_sum >= 10000:
    sum_sum = abs(10000 - steps_sum)
    print(f'Goal reached! Good job!\n{sum_sum} steps over the goal!')
else:
    print(f'{sum_sum} more steps to reach goal.')
