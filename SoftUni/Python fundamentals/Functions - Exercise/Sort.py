def sort_func(str_num: str):
    lst = str_num.split()
    lst = [int(_) for _ in lst]
    return sorted(lst)


print(sort_func(input()))
