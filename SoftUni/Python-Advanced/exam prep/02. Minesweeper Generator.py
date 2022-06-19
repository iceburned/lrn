n = int(input())


def is_outside(i, ii, size):
    return 0 <= i < size and 0 <= ii < size


def check(i, ii, mtx):
    count = 0
    if is_outside(i-1, ii, len(mtx)) and mtx[i-1][ii] == '*':  # up
        count += 1
    if is_outside(i-1, ii+1, len(mtx)) and mtx[i-1][ii+1] == '*':  # up-right
        count += 1
    if is_outside(i, ii+1, len(mtx)) and mtx[i][ii+1] == '*':  # right
        count += 1
    if is_outside(i+1, ii+1, len(mtx)) and mtx[i+1][ii+1] == '*':  # right-down
        count += 1
    if is_outside(i+1, ii, len(mtx)) and mtx[i+1][ii] == '*':  # down
        count += 1
    if is_outside(i+1, ii-1, len(mtx)) and mtx[i+1][ii-1] == '*':  # left-down
        count += 1
    if is_outside(i, ii-1, len(mtx)) and mtx[i][ii-1] == '*':  # left
        count += 1
    if is_outside(i-1, ii-1, len(mtx)) and mtx[i-1][ii-1] == '*':  # left-up
        count += 1
    return count


mtx = [[0 for s in range(n)] for _ in range(n)]

for _ in range(int(input())):
    mine = input().strip('()').split(', ')
    mtx[int(mine[0])][int(mine[1])] = '*'

for i in range(len(mtx)):
    for ii in range(len(mtx[i])):
        if mtx[i][ii] == '*':
            continue
        cell_value = check(i, ii, mtx)
        mtx[i][ii] = cell_value

for row in mtx:
    print(' '.join(map(str, row)))
