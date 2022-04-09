table = set()
for _ in range(int(input())):
    data = input().split(" ")
    [table.add(_) for _ in data]
[print(_) for _ in table]
