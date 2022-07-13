def odd_even(n):
    even = 0
    odd = 0
    for i in n:
        i = int(i)
        if i % 2 == 0:
            even += i
        elif i % 2 != 0:
            odd += i
    return even, odd


num = input()
c = odd_even(num)
print(f'Odd sum = {c[1]}, Even sum = {c[0]}')
