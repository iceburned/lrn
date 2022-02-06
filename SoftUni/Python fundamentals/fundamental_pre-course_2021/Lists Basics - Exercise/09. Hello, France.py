# items = input().split('|')
# budget = float(input())
# ticket = 0
# spend = budget
# data = []
# data1 = []
# for s in items:
#     data = s.split('->')
#     price = float(data[1])
#     if (budget + ticket) >= 150 or price > spend:
#         break
#     elif data[0] == 'Clothes':
#         if price <= 50:
#             spend -= price
#             ticket += price * 0.40
#             temp_price = price * 0.40
#             a = f'{price + temp_price:.2f}'
#             data1.append(a)
#         else:
#             pass
#     elif data[0] == 'Shoes':
#         if price <= 35:
#             spend -= price
#             ticket += price * 0.40
#             temp_price = price * 0.40
#             a = f'{price + temp_price:.2f}'
#             data1.append(a)
#         else:
#             pass
#     elif data[0] == 'Accessories':
#         if price <= 20.5:
#             spend -= price
#             ticket += price * 0.40
#             temp_price = price * 0.40
#             a = f'{price + temp_price:.2f}'
#             data1.append(a)
#         else:
#             pass
# print(' '.join(data1))
# print(f'Profit: {ticket:.2f}')
# if (budget + ticket) >= 150:
#     print('Hello, France!')
# else:
#     print('Not enough money.')


items = input().split('|')
budget = float(input())
data = []
profit = 0
spend = budget

def check_price(item_name, item_price):
    maximum_prices = {
        "Clothes": item_price <= 50,
        "Shoes": item_price <= 35,
        "Accessories": item_price <= 20.5
    }
    if maximum_prices[item_name]:
        return True

for i in items:
    data_split = i.split("->")
    item_name = data_split[0]
    item_price = float(data_split[1])
    if check_price(item_name, item_price):
        if spend >= item_price:
            spend -= item_price
            data.append(item_price * 1.4)
            profit += 0.4 * item_price

total_sum = profit + budget
new_price_formatted = [f'{_:.2f}' for _ in data]
print(*new_price_formatted)
print(f'Profit: {profit:.2f}')
if total_sum >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
