import re

data = input()
regex_num = r"\d+"
reg_num = re.findall(regex_num, data)
coolness = 1
for i in reg_num:
    for ii in i:
        ii = int(ii)
        coolness *= ii
print(f"Cool threshold: {coolness}")
regex = r"(\*\*|::)[A-Z][a-z][a-z]+\1"
reg_search = re.finditer(regex, data)
items = []
for zz in reg_search:
    items.append(zz.group())
dkt = {}
for s in items:
    num = 0
    complete = s
    s = s[2:-2]
    for ss in s:
        num += ord(ss)
    dkt.update({complete: num})
print(f"{len(items)} emojis found in the text. The cool ones are:")
for d, k in dkt.items():
    if k >= coolness:
        print(d)
