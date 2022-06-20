word = input()
mtx_size = int(input())
mtx = [[s for s in input()] for _ in range(mtx_size)]
p = ()
for i in range(mtx_size):
    for ii in range(mtx_size):
        if mtx[i][ii] == 'P':
            p = i, ii


def move(i, ii, comm):
    if comm == 'up':
        return i - 1, ii
    elif comm == 'right':
        return i, ii + 1
    elif comm == 'down':
        return i + 1, ii
    elif comm == 'left':
        return i, ii - 1


letters = word
num_commands = int(input())
for _ in range(num_commands):
    command = input()
    new_pos = move(p[0], p[1], command)
    if not 0 <= new_pos[0] <= mtx_size - 1 or not 0 <= new_pos[1] <= mtx_size - 1:
        if letters:
            letters = letters[:-1]
        continue
    if mtx[new_pos[0]][new_pos[1]].isalpha():
        letters = letters + mtx[new_pos[0]][new_pos[1]]
    mtx[p[0]][p[1]] = '-'
    mtx[new_pos[0]][new_pos[1]] = 'P'
    p = new_pos
print(letters)
for row in mtx:
    print(''.join(row))
