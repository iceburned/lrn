num = int(input())
flag = True
while flag:
    num += 1
    for i in str(num):
        if str(num).count(i) >= 2:
            pass
        else:
            asd = set(str(num))
            if len(asd) == len(str(num)):
                flag = False
print(num)
