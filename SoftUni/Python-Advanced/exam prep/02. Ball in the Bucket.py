mtx = [[s for s in input().split()] for _ in range(6)]
lst = []


def trow(cords, board):
    num = tuple(map(int, cords.strip('()').split(', ')))
    flag = False
    if (0 <= num[0] < 6 and 0 <= num[1] < 6) and board[num[0]][num[1]] == 'B':
        sum_sum = 0
        flag = True
        for i in range(6):
            if board[i][num[1]].isalpha():
                pass
            else:
                sum_sum += int(board[i][num[1]])
        return sum_sum, flag
    return 0, flag


checker = []
scores = 0
for _ in range(3):
    num = input()

    if num not in checker:
        points, flag = trow(num, mtx)
        scores += points
        if flag:
            checker.append(num)
    else:
        scores += 0

if scores >= 300:
    print(f"Good job! You scored {scores} points, and you've won Lego Construction Set.")
elif 200 <= scores <= 299:
    print(f"Good job! You scored {scores} points, and you've won Teddy Bear.")
elif 100 <= scores <= 199:
    print(f"Good job! You scored {scores} points, and you've won Football.")
elif scores < 100:
    print(f"Sorry! You need {100 - scores} points more to win a prize.")
