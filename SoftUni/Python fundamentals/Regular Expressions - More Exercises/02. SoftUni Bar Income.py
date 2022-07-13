import re

data = input()
total_sum = 0
while not data == "end of shift":
    regex = r"\%(?P<name>[A-Z][a-z]+)\%([^\|\$\%\.]*)\<(?P<product>\w+)\>([^\|\$\%\.]*)\|(?P<count>\d+)\|([^\|\$\%\.\d]*)(?P<price>\d+\.*\d+)\$"
    reg_answer = re.finditer(regex, data)
    for i in reg_answer:
        total_price = int(i.group("count")) * float(i.group("price"))
        total_sum += total_price
        print(f"{i.group('name')}: {i.group('product')} - {total_price:.2f}")
    data = input()
print(f"Total income: {total_sum:.2f}")
