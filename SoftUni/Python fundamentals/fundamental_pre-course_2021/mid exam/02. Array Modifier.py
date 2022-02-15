arr = [int(_) for _ in input().split(' ')]
command = input()


def swap(ind1, ind2, ar):
    ar[ind1], ar[ind2] = ar[ind2], ar[ind1]
    return ar


def multiply(ind1, ind2, ar):
    ar[ind1] = ar[ind1] * ar[ind2]
    return ar


def decrease(ar):
    ar = [(_ - 1) for _ in ar]
    return ar


while not command == 'end':
    if command == 'decrease':
        arr = decrease(arr)
    else:
        com, index1, index2 = command.split(' ')
        index1 = int(index1)
        index2 = int(index2)
        if com == "swap":
            arr = swap(index1, index2, arr)
        elif com == "multiply":
            arr = multiply(index1, index2, arr)
    command = input()

arr = [str(_) for _ in arr]
print(', '.join(arr))
