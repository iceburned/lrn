mtx_size = tuple(map(int, input().split(', ')))
mtx = [[x for x in input().split()] for _ in range(mtx_size[0])]

y = ()  # where i am
for i in range(mtx_size[0]):
    for ii in range(mtx_size[1]):
        if mtx[i][ii] == 'Y':
            y = i, ii


def move(y, comm, size):  # move in desired direction

    if comm == 'up':
        if y[0] == 0:
            return size[0] - 1, y[1]
        return y[0] - 1, y[1]
    elif comm == 'right':
        if y[1] == size[1] - 1:
            return y[0], 0
        return y[0], y[1] + 1
    elif comm == 'down':
        if y[0] == size[0] - 1:
            return 0, y[1]
        return y[0] + 1, y[1]
    elif comm == 'left':
        if y[1] == 0:
            return y[0], size[1] - 1
        return y[0], y[1] - 1


def content_check():  # check if C, G or D is left in mtx
    for s in range(mtx_size[0]):
        for ss in range(mtx_size[1]):

            if mtx[s][ss] == 'D' or mtx[s][ss] == 'G' or mtx[s][ss] == 'C':
                return True


# decorations, gifts, cookies
presents = [0, 0, 0]
data = input()
flag = False
while not data == 'End':
    comm, num = data.split('-')

    for x in range(int(num)):  # counting moves in direction one by one
        new_pos = move(y, comm, mtx_size)

        if mtx[new_pos[0]][new_pos[1]] == '.':
            mtx[y[0]][y[1]] = 'x'
            mtx[new_pos[0]][new_pos[1]] = 'Y'
        elif mtx[new_pos[0]][new_pos[1]] == 'x':
            mtx[y[0]][y[1]] = 'x'
            mtx[new_pos[0]][new_pos[1]] = 'Y'
        elif mtx[new_pos[0]][new_pos[1]] == 'D':
            mtx[y[0]][y[1]] = 'x'
            mtx[new_pos[0]][new_pos[1]] = 'Y'
            presents[0] += 1
        elif mtx[new_pos[0]][new_pos[1]] == 'G':
            mtx[y[0]][y[1]] = 'x'
            mtx[new_pos[0]][new_pos[1]] = 'Y'
            presents[1] += 1
        elif mtx[new_pos[0]][new_pos[1]] == 'C':
            mtx[y[0]][y[1]] = 'x'
            mtx[new_pos[0]][new_pos[1]] = 'Y'
            presents[2] += 1

        y = new_pos

        if not content_check():
            flag = True
            break
    if flag:
        break

    data = input()

if flag:
    print("Merry Christmas!")

print(f"You've collected:\n- {presents[0]} Christmas decorations\n- {presents[1]} Gifts\n- {presents[2]} Cookies")
[print(' '.join(_)) for _ in mtx]
