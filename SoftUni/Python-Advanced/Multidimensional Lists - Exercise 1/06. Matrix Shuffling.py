row, col = [int(_) for _ in input().split(" ")]
mtx = [[a for a in (input().split(" "))] for _ in range(row)]
data = input()
while not data == "END":
    flag = False
    if data.startswith("swap"):
        data = data[5:].split(" ")
        data = [int(_) for _ in data if int(_) >= 0]  # test if it's negative
        if len(data) == 4:  # test if length is different
            if data[0] < row and data[2] < row:  # test if index is in range
                if data[1] < col and data[3] < col:  # test if index is in range
                    flag = True
    if flag:
        mtx[data[0]][data[1]], mtx[data[2]][data[3]] = mtx[data[2]][data[3]], mtx[data[0]][data[1]]   # swap
        [print(*_) for _ in mtx]
    else:
        print("Invalid input!")
    data = input()
