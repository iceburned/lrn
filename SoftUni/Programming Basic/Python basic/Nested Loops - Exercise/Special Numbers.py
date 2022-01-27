n = int(input())
counter = 0
for num in range(1111, 9999 + 1):
    num = str(num)
    for i in num:
        i1 = int(i)
        if i1 == 0:
            pass
        else:
            if n % i1 == 0:
                counter += 1
    if counter == 4:
        print(num, end=' ')
        counter = 0
    else:
        counter = 0
