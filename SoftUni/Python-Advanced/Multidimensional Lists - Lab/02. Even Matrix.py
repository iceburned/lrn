mtx = []
for _ in range(int(input())):
    mtx.append([])
    for s in [int(_) for _ in input().split(", ") if int(_) % 2 == 0]:
        mtx[_].append(s)
print(mtx)
