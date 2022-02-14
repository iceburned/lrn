waiting_people = int(input())
lift_state = [int(_) for _ in input().split(' ')]
for i in range(len(lift_state)):
	for person in range(waiting_people):
		if lift_state[i] < 4:
			lift_state[i] += 1
			waiting_people -= 1
		else:
			break
flag = True
for s in lift_state:
    if not s == 4:
        flag = False
if flag and waiting_people == 0:
    pass
elif flag:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
else:
    print("The lift has empty spots!")
print(*lift_state)
