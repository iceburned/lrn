from collections import deque

cup_capacity = deque(int(_) for _ in input().split(" "))
bottle_capacity = deque(int(_) for _ in input().split(" "))
waste = 0
while any(cup_capacity) and any(bottle_capacity):
    cup_fill = bottle_capacity[-1] - cup_capacity[0]
    if cup_fill >= 0:
        waste += cup_fill
        cup_capacity.popleft()
        bottle_capacity.pop()
    else:
        if any(bottle_capacity):
            cup_capacity[0] = cup_capacity[0] - bottle_capacity[-1]
            bottle_capacity.pop()
if any(cup_capacity):
    print("Cups: ", end='')
    print(*cup_capacity)
elif any(bottle_capacity):
    print("Bottles: ", end='')
    print(*bottle_capacity)
print(f"Wasted litters of water: {waste}")
