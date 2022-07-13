lst = [int(_) for _ in input().split(' ')]
shoot = input()
while not shoot == "End":
    shoot = int(shoot)
    if shoot < len(lst):
        target = lst[shoot]
        if lst[shoot] != -1:
            lst[shoot] = -1
        for i in range(len(lst)):
            if not lst[i] == -1 and lst[i] > target:
                lst[i] -= target
            elif not lst[i] == -1 and lst[i] <= target:
                lst[i] += target
    shoot = input()
count = [_ for _ in lst if _ == -1]
print(f"Shot targets: {count.count(-1)} -> {' '.join(map(str, lst))}")
