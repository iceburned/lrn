from collections import deque


p = deque()
d = deque()
s = 0
sum_petrol = 0
sum_distance = 0
for _ in range(int(input())):
    petrol, distance = input().split(" ")
    p.append(int(petrol))
    d.append(int(distance))
for s in range(len(p)):
    if p[0] >= d[0]:
        break
    else:
        p.rotate(-1)
        d.rotate(-1)
for ss in range(len(p)):
    if sum_distance <= sum_petrol:
        sum_distance = d[ss]
        sum_petrol += p[ss]
        sum_petrol = sum_petrol - d[ss]
print(s)
