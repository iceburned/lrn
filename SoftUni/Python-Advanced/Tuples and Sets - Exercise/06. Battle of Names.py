set_odd = set()
set_even = set()
for i in range(1, int(input()) + 1):
    temp_num = 0
    name = input()
    for s in name:
        temp_num += ord(s)
    temp_num = temp_num // i
    if temp_num % 2 == 0:
        set_even.add(temp_num)
    else:
        set_odd.add(temp_num)
answer = []
if sum(set_odd) == sum(set_even):
    answer = set_odd.union(set_even)
elif sum(set_odd) > sum(set_even):
    answer = set_odd.difference(set_even)
elif sum(set_odd) < sum(set_even):
    answer = set_odd.symmetric_difference(set_even)
answer = [str(_) for _ in answer]
print(', '.join(answer))
