import re
data = input()
reg_str = r"^>>(?P<item>[A-Za-z]+)<<(?P<price>\d+\.?\d+)!(?P<count>\d+)$"
print('Bought furniture:')
sum_sum = 0
while not data == "Purchase":
    find_iter = re.finditer(reg_str, data)
    for i in find_iter:
        item = i.group('item')
        print(item)
        price = i.group('price')
        count = i.group('count')
        sum_sum += float(price) * int(count)
    data = input()
print(f"Total money spend: {sum_sum:.2f}")
