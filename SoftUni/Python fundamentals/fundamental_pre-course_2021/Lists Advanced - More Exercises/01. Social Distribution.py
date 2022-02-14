def social_distrib(l, m):
    temp_add = 0
    for i in range(len(l)):
        if l[i] < m:
            temp_add = m - l[i]
            l[i] += temp_add
            l_max = l.index(max(l))
            l[l_max] -= temp_add
    return l


lst = [int(_) for _ in input().split(', ')]
min_wealth = int(input())
social_distrib(lst, min_wealth)
if sum(lst) >= len(lst) * min_wealth:
    print(lst)
else:
    print("No equal distribution possible")
