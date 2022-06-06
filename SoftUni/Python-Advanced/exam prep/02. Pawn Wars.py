board = [input().split() for _ in range(8)]
board = list(reversed(board))


def find_position(player, mtx):  # position of pawn
    for pos_row in range(8):
        for pos_col in range(8):
            if mtx[pos_row][pos_col] == player:
                return pos_row, pos_col


# white, black pawns from board in starting positions
white_pos_row, white_pos_col = find_position("w", board)
black_pos_row, black_pos_col = find_position("b", board)


def check_diagonally_white(w_row, w_col, b_row, b_col):  # take opposite pawn if in close diagonal position
    left_row = w_row + 1                                         # for white
    left_col = w_col - 1
    right_row = w_row + 1
    right_col = w_col + 1

    if left_row == b_row and left_col == b_col:  # check in front left
        w_row = left_row
        w_col = left_col
        b_row = None
        b_col = None
    elif right_row == b_row and right_col == b_col:  # check in front right
        w_row = right_row
        w_col = right_col
        b_row = None
        b_col = None

    return w_row, w_col, b_row, b_col


def check_diagonally_black(w_row, w_col, b_row, b_col):  # # take opposite pawn if in close diagonal position
    left_row = b_row - 1                                          # for black
    left_col = b_col - 1
    right_row = b_row - 1
    right_col = b_col + 1

    if left_row == w_row and left_col == w_col:  # check in front left
        b_row = left_row
        b_col = left_col
        w_row = None
        w_col = None
    elif right_row == w_row and right_col == w_col:  # check in front right
        b_row = right_row
        b_col = right_col
        w_row = None
        w_col = None

    return w_row, w_col, b_row, b_col


# when pawn is taken then check for None value, this will be used forward
def pawn_taken_none(white_row, white_col, black_row, black_col):
    white = any(filter(None, [white_row, white_col]))
    black = any(filter(None, [black_row, black_col]))
    return black, white


# last conversion for chess readable output  - a1, b3 ....
def board_position(position_row, position_col):
    dkt = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    return dkt[position_col] + str(position_row + 1)


queen = ''
pawn_win = ''
position = ''
while True:
    turn = 'w'  # check for which turn is it
    # check if in diagonally position pawn is present
    white_pos_row, white_pos_col, black_pos_row, black_pos_col = \
        check_diagonally_white(white_pos_row, white_pos_col, black_pos_row, black_pos_col)
    # check if pawn is taken (None value) and return bool for comparison in next check
    black, white = pawn_taken_none(white_pos_row, white_pos_col, black_pos_row, black_pos_col)

    if not black:  # if black pawn is taken
        pawn_win = 'White'
        position = board_position(white_pos_row, white_pos_col)
        break

    # move white forward
    white_pos_row, white_pos_col = white_pos_row + 1, white_pos_col

    if white_pos_row == 7:  # row 8 for promoting to queen is reached
        queen = "White"
        position = board_position(white_pos_row, white_pos_col)
        break

    turn = 'b'  # check for which turn is it
    # check if in diagonally position pawn is present
    white_pos_row, white_pos_col, black_pos_row, black_pos_col = \
        check_diagonally_black(white_pos_row, white_pos_col, black_pos_row, black_pos_col)
    # check if pawn is taken (None value) and return bool for comparison in next check
    black, white = pawn_taken_none(white_pos_row, white_pos_col, black_pos_row, black_pos_col)

    if not white:  # if black pawn is taken
        pawn_win = "Black"
        position = board_position(black_pos_row, black_pos_col)
        break

    # move black forward
    black_pos_row, black_pos_col = black_pos_row - 1, black_pos_col

    if black_pos_row == 0:  # row 1 for promoting to queen is reached
        queen = "Black"
        position = board_position(black_pos_row, black_pos_col)
        break

if queen:
    print(f"Game over! {queen} pawn is promoted to a queen at {position}.")
else:
    print(f"Game over! {pawn_win} win, capture on {position}.")
