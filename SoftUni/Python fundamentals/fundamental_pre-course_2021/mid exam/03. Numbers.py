lst = [int(_) for _ in input().split(' ')]
avg = sum(lst) / len(lst)
new_lst = sorted([_ for _ in lst if _ > avg], reverse=True)
result = None
if new_lst:
    result = ' '. join(map(str, new_lst[:5]))
else:
    result = "No"
print(result)
