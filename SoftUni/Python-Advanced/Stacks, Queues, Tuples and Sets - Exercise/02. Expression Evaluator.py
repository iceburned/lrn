from math import floor

lst = [_ for _ in input().split(' ')]
nums = []
for i in lst:
    if i.lstrip('-').isdigit():
        nums.append(i)
    else:
        temp_num = eval(i.join(nums))
        temp_num = floor(temp_num)
        nums.clear()
        nums.append(str(temp_num))
print(*nums)
