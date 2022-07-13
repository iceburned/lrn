import re
data = input().lower()
key = "\\b" + input().lower() + "\\b"
answer = re.findall(key, data)
count = 0
for i in answer:
    count += 1
print(count)

# drug variant
# key = rf"\b{input().lower()}\b"
# print(len(re.findall(key,data)
