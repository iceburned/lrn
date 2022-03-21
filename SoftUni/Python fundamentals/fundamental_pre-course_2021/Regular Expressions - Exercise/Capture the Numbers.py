import re
data = input()
reg_str = r"\d+"
while data:
    answer = re.findall(reg_str, data)
    for i in answer:
        print(''.join(i), end=' ')
    data = input()
