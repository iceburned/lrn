energy = int(input())
distance = input()
count_moves = 0
flag = True
while distance != "End of battle":
    distance = int(distance)
    if energy - distance >= 0:
        count_moves += 1
        energy -= distance
    elif energy - distance < 0:
        print(f"Not enough energy! Game ends with {count_moves} won battles and {energy} energy")
        flag = False
        break
    if count_moves % 3 == 0:
        energy += count_moves
    distance = input()
if flag:
    print(f"Won battles: {count_moves}. Energy left: {energy}")
