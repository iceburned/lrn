board = [input().split() for _ in range(8)]


def find_position(player, mtx):
    for pos_row in range(8):
        for pos_col in range(8):
            if mtx[pos_row][pos_col] == player:
                return pos_row, pos_col


white_pos_row, white_pos_col = find_position("w", board)
black_pos_row, black_pos_col = find_position("b", board)


def check_diagonally_white(w_row, w_col, b_row, b_col):
    left_row = w_row + 1
    left_col = w_col - 1
    right_row = w_row + 1
    right_col = w_col + 1
    if left_row == b_row and left_col == b_col:
        w_row = left_row
        w_col = left_col
        b_row = None
        b_col = None
    elif right_row == b_row and right_col == b_col:
        w_row = right_row
        w_col = right_col
        b_row = None
        b_col = None
    return w_row, w_col, b_row, b_col


def check_diagonally_black(w_row, w_col, b_row, b_col):
    left_row = b_row - 1
    left_col = b_col - 1
    right_row = b_row - 1
    right_col = b_col + 1
    if left_row == w_row and left_col == w_col:
        b_row = left_row
        b_col = left_col



def pawn_taken_none(white_row, white_col, black_row, black_col):
    white = any(filter(lambda x: x is None, [white_row, white_col]))
    black = any(filter(lambda x: x is None, [black_row, black_col]))
    return white, black


while True:
    turn = 'w'
    white_pos_row, white_pos_col, black_pos_row, black_pos_col = \
        check_diagonally_white(white_pos_row, white_pos_col, black_pos_row, black_pos_col)
    black, white = pawn_taken_none(white_pos_row, white_pos_col, black_pos_row, black_pos_col)

    if white:
        break

    # move white forward
    white_pos_row, white_pos_col = white_pos_row + 1, white_pos_col

    if white_pos_row == 7:  # row 8 for promoting to queen is reached
        break

    turn = 'b'
    white_pos_row, white_pos_col, black_pos_row, black_pos_col = \
        check_diagonally_black(white_pos_row, white_pos_col, black_pos_row, black_pos_col)