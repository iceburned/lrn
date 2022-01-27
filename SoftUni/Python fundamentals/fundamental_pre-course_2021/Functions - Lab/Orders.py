def orders(product, cnt):
    if product == 'coffee':
        return cnt * 1.50
    elif product == 'water':
        return cnt * 1.00
    elif product == 'coke':
        return cnt * 1.40
    elif product == 'snacks':
        return cnt * 2.00
product = input()
cnt = int(input())
print(f'{(orders(product, cnt)):.2f}')
