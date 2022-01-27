# def first(a):
#     if a == 0 or a == 1 or a == 2:
#         return 1
#     elif a == 3:
#         return 2
#     else:
#         return (first(a - 1) +
#                 first(a - 2) +
#                 first(a - 3))
#
#
# def second(a):
#     for i in range(1, a + 1):
#         print(first(i), end=' ')
#
#
# second(int(input()))
