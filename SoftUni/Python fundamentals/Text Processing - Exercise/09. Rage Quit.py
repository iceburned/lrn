import re

text = input()
numbers = re.findall(r'\d+', text)
new_text = ""

for num in numbers:
    position = text.find(num)
    new_text += text[:position].upper() * int(num)
    text = text.replace(text[:position + len(num)], "")

unique = "".join(set(new_text))

print(f"Unique symbols used: {len(unique)}")
print(new_text)
