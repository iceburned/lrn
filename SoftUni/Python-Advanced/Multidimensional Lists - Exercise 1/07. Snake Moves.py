from collections import deque

row, col = map(int, input().split(" "))
data = deque(input())
mtx = []
for s in range(row):
    mtx.append([])
    if s % 2 == 0:
        for ss in range(col):
            mtx[s].append(data[0])
            data.rotate(-1)
    else:
        for ss in range(col):
            mtx[s].append(data[0])
            data.rotate(-1)
        mtx[s].reverse()
[print(''.join(_)) for _ in mtx]
