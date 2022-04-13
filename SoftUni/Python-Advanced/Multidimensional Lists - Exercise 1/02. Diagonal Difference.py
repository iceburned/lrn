mtx = []
for _ in range(int(input())):
    mtx.append(input().split(" "))
prim_diag = sum([int(mtx[_][_]) for _ in range(len(mtx))])
sec_diag = sum([int(mtx[_][-_-1]) for _ in range(len(mtx))])
answer = abs(prim_diag - sec_diag)
print(answer)
