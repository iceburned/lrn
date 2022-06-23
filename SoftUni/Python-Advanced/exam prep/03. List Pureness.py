from collections import deque


def pureness(lst):
    el_sum = sum([i * lst[i] for i in range(len(lst))])
    return el_sum


def best_list_pureness(*args):
    pur = {}
    data = args
    lst = deque(data[0])
    rotate = data[1]
    pur.update({0: pureness(lst)})
    for i in range(1, rotate + 1):
        lst.rotate(1)
        pur.update({i: pureness(lst)})
    max_el = sorted(pur.items(), key=lambda v: v[1], reverse=True)
    return f"Best pureness {max_el[0][1]} after {max_el[0][0]} rotations"


#
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)