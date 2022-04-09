lst = []
for _ in range(int(input())):
    first_set = set()
    second_set = set()
    first, second = input().split("-")
    first_1, first_2 = first.split(",")
    second_1, second_2 = second.split(",")
    [first_set.add(_) for _ in range(int(first_1), int(first_2) + 1)]
    [second_set.add(_) for _ in range(int(second_1), int(second_2) + 1)]
    intersection = first_set.intersection(second_set)
    lst.append(intersection)
lst = sorted(lst, key=lambda x: len(x))
print(f"Longest intersection is {list(lst[-1])} with length {len(lst[-1])}")
