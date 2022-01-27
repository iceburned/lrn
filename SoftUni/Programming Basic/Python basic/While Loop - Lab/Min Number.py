import sys
max_ss = sys.maxsize
while True:
    num = input()
    if num == "Stop":
        break
    num1 = int(num)
    if num1 < max_ss:
        max_ss = num1
print(max_ss)
