import re
data = input()
reg_ex = r"\b_(?P<words>[A-Za-z0-9]+)\b"
answer = re.finditer(reg_ex, data)
valid_variable = []
for i in answer:
    valid_variable.append(i.group('words'))
print(','.join(valid_variable))
