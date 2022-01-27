import sys

count = int(input())
num_max = -sys.maxsize
num_min = sys.maxsize
for i in range(0, count):
    num = int(input())
    if num < num_min:
        num_min = num
    if num > num_max:
        num_max = num

print(f'Max number: {num_max}')
print(f'Min number: {num_min}')
