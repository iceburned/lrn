row, col = map(int, input().split(" "))
mtx = [[int(_) for _ in input().split(" ")] for _ in range(row)]
temp_lst = None
sum_sum = 0
for s in range(len(mtx) - 2):
    for ss in range(col - 2):
        row_1 = [mtx[s][ss], mtx[s][ss + 1], mtx[s][ss + 2]]
        row_2 = [mtx[s + 1][ss], mtx[s + 1][ss + 1], mtx[s + 1][ss + 2]]
        row_3 = [mtx[s + 2][ss], mtx[s + 2][ss + 1], mtx[s + 2][ss + 2]]
        sum_all = sum(row_1) + sum(row_2) + sum(row_3)
        if sum_all >= sum_sum:
            sum_sum = sum_all
            temp_lst = [row_1, row_2, row_3]
print(f"Sum = {sum_sum}")
[print(*_) for _ in temp_lst]
