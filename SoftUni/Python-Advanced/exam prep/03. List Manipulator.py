def list_manipulator(lst, *args):
    temp = list(args)
    lst_temp = temp[2:]
    if temp[0] == "add":
        if temp[1] == "beginning":
            return lst_temp + lst
        elif temp[1] == "end":
            return lst + lst_temp
    elif temp[0] == "remove":
        if temp[1] == "beginning":
            if lst_temp:
                return lst[lst_temp[0]:]
            return lst[1:]
        elif temp[1] == "end":
            if lst_temp:
                return lst[:-lst_temp[0]]
            return lst[:-1]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))