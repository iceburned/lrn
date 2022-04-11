mtx = []
col, row = input().split(", ")
col = int(col)
row = int(row)
for s in range(int(col)):
    mtx.append([int(_) for _ in input().split(" ")])
sum_sum = 0
for i in range(row):
    for a in range(col):
        sum_sum += mtx[a][i]
    print(sum_sum)
    sum_sum = 0
