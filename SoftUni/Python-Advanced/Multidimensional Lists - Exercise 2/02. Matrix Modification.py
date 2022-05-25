mtx = [input().split(' ') for _ in range(int(input()))]
for i in range(len(mtx)):
    for ii in range(len(mtx[i])):
        mtx[i][ii] = int(mtx[i][ii])
data = input()
while data != "END":
    comm, row_index, col_index, val = data.split(' ')
    row_index = int(row_index)
    col_index = int(col_index)
    val = int(val)
    if comm == "Add":
        if 0 <= row_index < len(mtx) > col_index >= 0:
            mtx[row_index][col_index] += val
        else:
            print("Invalid coordinates")
    else:
        if 0 <= row_index < len(mtx) > col_index >= 0:
            mtx[row_index][col_index] -= val
        else:
            print("Invalid coordinates")
    data = input()
[print(*_) for _ in mtx]
