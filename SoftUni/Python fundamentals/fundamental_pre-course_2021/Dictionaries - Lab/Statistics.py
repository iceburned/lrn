pair = input().split(': ')
dkt = {}
total_products = 0
total_quantity = 0
while "statistics" not in pair:
    total_products += 1
    key, value = pair
    total_quantity += int(value)
    if key in dkt:
        dkt[key] += int(value)
        total_products -= 1
    else:
        dkt[key] = int(value)
    pair = input().split(': ')
print('Products in stock:')
[print('- ' + _ + ':', dkt[_]) for _ in dkt]
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
