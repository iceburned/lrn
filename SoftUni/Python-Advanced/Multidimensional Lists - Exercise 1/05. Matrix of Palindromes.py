row, col = [int(_) for _ in input().split(" ")]
mtx = []
for s in range(row):
    mtx.append([])
    for ss in range(col):
        index = ord("a")
        mtx[s].append(chr(index + s) + chr(index + ss + s) + chr(index + s))
[print(*_) for _ in mtx]
