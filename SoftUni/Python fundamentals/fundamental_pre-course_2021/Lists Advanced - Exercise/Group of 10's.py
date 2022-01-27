lst = list(map(int, input().split(', ')))
lst_max = 0
if max(lst) % 10 == 0:
    lst_max = max(lst) - 1
else:
    lst_max = max(lst)
lst_sum = []
for a in range(1, (lst_max // 10) + 2):
    for b in lst:
        if (a * 10) - 10 < b < (a * 10 + 1):
            lst_sum.append(b)
    print(f"Group of {a * 10}'s: {lst_sum}")
    lst_sum = []
