n = input().split()
number_inverted = []
for num in n:
    numbers_inverted = int(num) * -1
    number_inverted.append(numbers_inverted)
print(number_inverted)

# n = input()
# lst = n.split()
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# for s in range(len(lst)):
#     if lst[s] >= 0:
#         lst[s] = -abs(lst[s])
#     else:
#         lst[s] = abs(lst[s])
# print(lst)
