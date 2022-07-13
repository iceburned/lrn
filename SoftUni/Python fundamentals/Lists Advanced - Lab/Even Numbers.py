lst = list(map(lambda _: int(_), input().split(", ")))
print([_ for _ in range(len(lst)) if lst[_] % 2 == 0])
