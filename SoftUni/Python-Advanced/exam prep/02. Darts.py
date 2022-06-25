first, second = input().split(', ')
mtx = [[int(s) if s.isdigit() else s for s in input().split()] for _ in range(7)]


def directions(cord, mtx):
    sum_sum = mtx[cord[0]][0] + mtx[cord[0]][6] + mtx[cord[1]][0] + mtx[cord[1]][6]
    return sum_sum


def hit(cord, board):
    if board[cord[0]][cord[1]].isnumeric():
        return board[cord[0]][cord[1]]
    elif board[cord[0]][cord[1]] == 'D':
        return (directions(cord, board)) * 2
    elif board[cord[0]][cord[1]] == 'T':
        return (directions(cord, board)) * 3


score_1 = 501
score_2 = 501
counter_1 = 0
counter_2 = 0
counter = 0
cord = ()
while True:
    cords = input()
    if cords:
        cord = tuple(map(int, cords.strip('()').split(', ')))
    else:
        break

    if not 0 <= cord[0] <= 6 or not 0 <= cord[1] <= 6:
        continue

    counter += 1
    if counter % 2 != 0:
        # first
        counter_2 += 1

        if mtx[cord[0]][cord[1]] == 'B':
            print(f'{first} won the game with {counter} throws!')
            break
        score_2 -= hit(cord, mtx)

    else:
        # second
        counter_1 += 1

        if mtx[cord[0]][cord[1]] == 'B':
            print(f'{second} won the game with {counter} throws!')
            break
        score_1 -= hit(cord, mtx)

    if score_2 <= 0:
        print(f'{first} won the game with {counter_2} throws!')
        break
    elif score_1 <= 0:
        print(f'{second} won the game with {counter_1} throws!')
        break

