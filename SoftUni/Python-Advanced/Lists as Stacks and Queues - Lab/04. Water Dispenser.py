from collections import deque


water = int(input())
queue = deque()
data = input()
while not data == "Start":
    queue.append(data)
    data = input()
data = input()
while not data == "End":
    if data.startswith("refill"):
        refill = data.split(" ")
        refill = int(refill[1])
        water += int(refill)
    else:
        data = int(data)
        if data <= water:
            person = queue.popleft()
            water -= data
            print(f"{person} got water")
        else:
            person = queue.popleft()
            print(f"{person} must wait")
    data = input()
print(f"{water} liters left")
