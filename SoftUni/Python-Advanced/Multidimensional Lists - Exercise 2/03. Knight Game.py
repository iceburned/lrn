def check_moves(mtx, row, col):
    temp_index = 0
    if len(mtx) > row - 2 >= 0 and len(mtx[0]) > col - 1 >= 0:  # up left
        if mtx[row - 2][col - 1] == "K":
            temp_index += 1
    if len(mtx) > row - 2 >= 0 and len(mtx[0]) > col + 1 >= 0:  # up right
        if mtx[row - 2][col + 1] == "K":
            temp_index += 1
    if len(mtx) > row - 1 >= 0 and len(mtx[0]) > col + 2 >= 0:  # right up
        if mtx[row - 1][col + 2] == "K":
            temp_index += 1
    if len(mtx) > row + 1 >= 0 and len(mtx[0]) > col + 2 >= 0:  # right down
        if mtx[row + 1][col + 2] == "K":
            temp_index += 1
    if len(mtx) > row + 2 >= 0 and len(mtx[0]) > col + 1 >= 0:  # down right
        if mtx[row + 2][col + 1] == "K":
            temp_index += 1
    if len(mtx) > row + 2 >= 0 and len(mtx[0]) > col - 1 >= 0:  # down left
        if mtx[row + 2][col - 1] == "K":
            temp_index += 1
    if len(mtx) > row + 1 >= 0 and len(mtx[0]) > col - 2 >= 0:  # left down
        if mtx[row + 1][col - 2] == "K":
            temp_index += 1
    if len(mtx) > row - 1 >= 0 and len(mtx[0]) > col - 2 >= 0:  # left up
        if mtx[row - 1][col - 2] == "K":
            temp_index += 1
    return temp_index


def main(mtx):
    horses = []
    for row in range(len(mtx)):
        temp_index = 0
        temp_col = 0
        for col in range(len(mtx[row])):
            if mtx[row][col] == "K":
                temp_col = col
                temp_index = check_moves(mtx, row, col)
                horses.append([])
                horses[-1].append(row)
                horses[-1].append(temp_col)
                horses[-1].append(temp_index)
    return horses


mtx = [[s for s in input()] for _ in range(int(input()))]
count_horses = 0
while True:
    horses = main(mtx)
    horses = sorted(horses, key=lambda x: x[2], reverse=True)
    zeros = any(filter(lambda x: x[2] != 0, horses))
    if zeros:
        mtx[horses[0][0]][horses[0][1]] = 0
        horses.pop(0)
        horses.clear()
        count_horses += 1
    else:
        break
print(count_horses)
