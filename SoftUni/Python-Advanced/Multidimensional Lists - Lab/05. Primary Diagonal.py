mtx = []
for _ in range(int(input())):
    mtx.append([int(_) for _ in input().split(" ")])
num = 0
for i in range(len(mtx)):
    num += mtx[i][i]
print(num)
