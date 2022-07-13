# import math
# lst = []
# [lst.append(input()) for _ in range(3)]
# lst = [int(_) for _ in lst]
# if math.prod(lst) > 0:
#     print("positive")
# else:
#     print("negative")


def multi(num1, num2, num3):
    num_sum = 0
    num_num = 0
    if num1 >= 0:
        for _ in range(num1):
            num_sum += num2
    else:
        for _ in range(0, num1, -1):
            num_sum += -num2
    if num3 >= 0:
        for _ in range(num3):
            num_num += num_sum
    else:
        for _ in range(0, num3, -1):
            num_num += -num_sum
    if num_num > 0:
        print('positive')
    else:
        print("negative")


num1 = int(input())
num2 = int(input())
num3 = int(input())

multi(num1, num2, num3)
