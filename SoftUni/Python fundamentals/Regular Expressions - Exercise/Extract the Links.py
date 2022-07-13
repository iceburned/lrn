import re
data = input()
reg_ex = r"w{3}\.[A-Za-z\d-]+(\-[A-Za-z0-9])*(\.[a-z]+)+"
valid_url = []
while data != '':
    answer = re.finditer(reg_ex, data)
    for i in answer:
        valid_url.append(i.group())
    data = input()
for url in valid_url:
    print(url)
