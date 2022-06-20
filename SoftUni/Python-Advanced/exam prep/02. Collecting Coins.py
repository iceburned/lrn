from math import floor

num = int(input())
mtx = [[int(s) if s.isdigit() else s for s in input().split()] for _ in range(num)]

p = ()
for i in range(len(mtx)):
    for ii in range(len(mtx[i])):
        if mtx[i][ii] == 'P':
            p = i, ii


def move(row, col, comm, num):
    if comm == 'up':
        if row == 0:
            return num - 1, col
        return row - 1, col
    elif comm == 'right':
        if col == num - 1:
            return row, 0
        return row, col + 1
    elif comm == 'down':
        if row == num - 1:
            return 0, col
        return row + 1, col
    elif comm == 'left':
        if col == 0:
            return row, num - 1
        return row, col - 1


lst = []
lst.append([p[0], p[1]])
coins = 0
command = input()
while command:
    n_pos = move(p[0], p[1], command, num)
    lst.append([n_pos[0], n_pos[1]])
    if mtx[n_pos[0]][n_pos[1]] == 'X':
        coins = floor(coins / 2)
        break
    else:
        coins += mtx[n_pos[0]][n_pos[1]]
        mtx[n_pos[0]][n_pos[1]] = 'P'
        mtx[p[0]][p[1]] = 0
    if coins >= 100:
        break
    p = n_pos
    command = input()
if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print('Your path:')
[print(_) for _ in lst]
