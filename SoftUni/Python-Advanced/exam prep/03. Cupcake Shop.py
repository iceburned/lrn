def stock_availability(*args):
    lst = args[0]
    command = args[1]
    list_2 = list(args[2:])
    new_lst = []
    if command == "delivery":
        return lst + list_2  # always at least one ?
    elif command == "sell":
        if list_2:
            for x in list_2:
                if str(x).isdigit():
                    if len(lst) >= int(x):
                        new_lst = lst[int(x):]
                    else:
                        new_lst = []
                else:
                    for i in list_2:
                        for ii in lst:
                            if i != ii:
                                new_lst.append(ii)
            return new_lst
        else:
            return lst[1:]



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))