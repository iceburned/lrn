lst = input().split()
lst = [int(_) for _ in lst]
num = int(input())
i = -1
lst1 = []
while lst:
    for a in range(num):
        i += 1
        if i == len(lst):
            i = 0
    lst1.append(lst.pop(i))
    i -= 1
lst1 = [str(_) for _ in lst1]
lst2 = ','.join(lst1)
print(f'[{lst2}]')


# numbers = [int(n) for n in input().split()]
# index, new_numbers, counter = -1, [], int(input())
# while len(numbers) > 0:
#     for _ in range(counter):
#         index += 1
#         if index == len(numbers):
#             index = 0
#
#     new_numbers.append(numbers.pop(index))
#     index -= 1
#
# new_numbers = repr(new_numbers).replace(" ", "")
# print(new_numbers)