board = []
[board.append(input().split()) for _ in range(8)]
king = tuple()
for s in range(len(board)):
    for ss in range(len(board[s])):
        if board[s][ss] == 'K':
            king = s, ss

directions = {
    'up': (-1, 0),
    'up-right': (-1, 1),
    'right': (0, +1),
    'right-down': (+1, +1),
    'down': (+1, 0),
    'left-down': (+1, -1),
    'left': (0, -1),
    'up-left': (-1, -1)
}
queens = []
for key, v in directions.items():
    king_temp = king
    while True:
        k = king_temp[0] + v[0], king_temp[1] + v[1]
        if not 0 <= k[0] <= 7 or not 0 <= k[1] <= 7:
            break
        elif board[k[0]][k[1]] == "Q":
            queens.append(list(k))
            break
        king_temp = k
if queens:
    [print(_) for _ in queens]
else:
    print('The king is safe!')
