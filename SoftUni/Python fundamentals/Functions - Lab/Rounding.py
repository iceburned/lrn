def rounding(lst):
    lst = [float(_).__round__() for _ in lst]
    return lst


lst_one = input().split()
print(rounding(lst_one))
