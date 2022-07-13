import re
data = input()
reg_str = r"(?<!-|_|\.)\b([A-Za-z\d]+)\b([-_.][A-" \
          r"Za-z\d]+)?@[a-z]+[-.][a-z]+([-.][a-z]+)?([.][a-z]+)?"
answer = re.finditer(reg_str, data)
for i in answer:
    print(i.group())
