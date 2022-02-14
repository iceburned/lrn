def shoot(l, i, v):
    if len(l) >= i:
        l[i] -= v
        if l[i] <= 0:
            l.pop(i)
    return l


def add(l, i, v):
    if len(l) <= i + 1:
        print("Invalid placement!")
    else:
        l.insert(i, v)
        return l


def strike(l, i, v):
    if (i+v) <= len(l) and (i-v) >= 0:
        for a in range(i + 1, i + v + 1):
            l[a] = 'Null'
        for b in range(i - 1, i - 1 - v, -1):
            l[b] = 'Null'
        l[i] = 'Null'
        new_list = [_ for _ in l if _ != 'Null']
        return new_list
    print("Strike missed!")
    return l


lst = [int(_) for _ in input().split(' ')]
damage_target = input()
answer = []
while not damage_target == 'End':
    action, index, value = damage_target.split(' ')
    index = int(index)
    value = int(value)
    if action == 'Shoot':
        shoot(lst, index, value)
    elif action == 'Add':
        add(lst, index, value)
    elif action == 'Strike':
        answer = strike(lst, index, value)

    damage_target = input()
answer = [str(_) for _ in answer]
print('|'.join(answer))
