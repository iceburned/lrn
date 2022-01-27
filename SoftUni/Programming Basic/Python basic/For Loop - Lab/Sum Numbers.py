s = int(input())
ss = 0
for i in range(0, s):
    num = int(input())
    if num:
        ss += num
    else:
        break
print(ss)
