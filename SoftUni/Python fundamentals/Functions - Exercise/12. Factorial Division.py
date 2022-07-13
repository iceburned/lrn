def factorial(n):
    b = n
    for i in range(1, n):
        b *= i
    return b


num = int(input())
num2 = int(input())
print(f'{factorial(num) / factorial(num2):.2f}')
