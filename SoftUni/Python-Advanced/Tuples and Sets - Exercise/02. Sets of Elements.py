set_1 = set()
set_2 = set()
first, second = input().split(" ")
[set_1.add(input()) for _ in range(int(first))]
[set_2.add(input()) for _ in range(int(second))]
diff = set_1.intersection(set_2)
[print(_) for _ in diff]
