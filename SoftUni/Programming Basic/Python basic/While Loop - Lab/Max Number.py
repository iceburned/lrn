# import sys
# num = input()
# number = 0
# num1 = -sys.maxsize
# while num != 'stop':
#
#     if num >= number:
#         num = number
#     number = input()
# print(num)

inpt =input()
max = - 10000000000000
while inpt != 'Stop':
    num = int(input())
    if num > max:
        max = num
    inpt = input()

print(max)
