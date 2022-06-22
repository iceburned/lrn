from collections import deque

fireworks = deque(int(_) for _ in input().split(', '))
exp_power = [int(_) for _ in input().split(', ')]

# palm, willow, crossette
lst = [0, 0, 0]
while fireworks and exp_power:
    f = fireworks.popleft()
    e = exp_power.pop()
    if f <= 0:
        exp_power.append(e)
        continue
    elif e <= 0:
        fireworks.appendleft(f)
        continue
    sum_sum = f + e
    if sum_sum % 3 == 0 and sum_sum % 5 == 0:
        lst[2] += 1
    elif sum_sum % 3 == 0:
        lst[0] += 1
    elif sum_sum % 5 == 0:
        lst[1] += 1
    else:
        fireworks.append(f - 1)
        exp_power.append(e)
    if all([True if _ >= 3 else False for _ in lst]):
        break
if all([True if _ >= 3 else False for _ in lst]):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join(map(str, fireworks))}")
if exp_power:
    print(f"Explosive Power left: {', '.join(map(str, exp_power))}")
print(f"Palm Fireworks: {lst[0]}\nWillow Fireworks: {lst[1]}\nCrossette Fireworks: {lst[2]}")
