def even_odd(*args):
    even = []
    odd = []
    data = args
    for s in data[:-1]:
        if s % 2 == 0:
           even.append(s)
        else:
            odd.append(s)
    if data[-1] == "even":
        return even
    elif data[-1] == "odd":
        return odd



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))