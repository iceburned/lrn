row, col = [int(_) for _ in input().split(" ")]
mtx = [[a for a in input().split(" ")] for _ in range(row)]
count = 0
for s in range(row - 1):
    for ss in range(col - 1):
        if mtx[s][ss] == mtx[s][ss + 1] == mtx[s + 1][ss] == mtx[s + 1][ss + 1]:
            count += 1
print(count)
