import re
data = input()
reg_str = r"\d"
a = ''
while data:
    answer = re.findall(reg_str, data)
    for i in answer:
        a += ''.join(i)
    print(a, end=' ')
    data = input()
    a = ''
