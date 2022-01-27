output = filter(lambda _: True if _ % 2 == 0 else False, [int(_) for _ in input().split()])
print([i for i in output], end='')
