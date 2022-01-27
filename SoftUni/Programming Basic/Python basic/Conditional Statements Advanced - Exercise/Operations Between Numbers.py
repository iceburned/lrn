n1 = int(input())
n2 = int(input())
operator = str(input())

n3 = 0
if n2 != 0:
    if operator == "+":
        n3 = n1 + n2
    elif operator == "-":
        n3 = n1 - n2
    elif operator == "*":
        n3 = n1 * n2
    elif operator == "/":
        n3 = f'{(n1 / n2):.2f}'
    elif operator == "%":
        n3 = n1 % n2
    if operator == "+" or operator == "-" or operator == "*":
        number = ''
        if n3 % 2 == 0:
            number = 'even'
        else:
            number = 'odd'
        print(f'{n1} {operator} {n2} = {n3} - {number}')
    else:
        print(f'{n1} {operator} {n2} = {n3}')
else:
    print(f'Cannot divide {n1} by zero')
