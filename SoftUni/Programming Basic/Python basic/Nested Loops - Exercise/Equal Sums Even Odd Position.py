first_num = int(input())
second_num = int(input())

count = 0
odd = 0
even = 0
for num in range(first_num, second_num + 1):
    for n in str(num):
        n = int(n)
        count += 1
        if count % 2 == 0:
            even += n
        else:
            odd += n
    if odd == even:
        print(num, end=' ')
        odd = 0
        even = 0
        count = 0
    else:
        odd = 0
        even = 0
        count = 0
