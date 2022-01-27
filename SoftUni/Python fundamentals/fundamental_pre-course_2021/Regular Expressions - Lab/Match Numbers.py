import re
data = input()
reg_str = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
valid_num = re.finditer(reg_str, data)
valid_num = [num.group() for num in valid_num]
print(*valid_num)
