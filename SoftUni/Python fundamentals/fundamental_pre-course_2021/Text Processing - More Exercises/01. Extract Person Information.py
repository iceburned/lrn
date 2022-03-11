import re

counter = int(input())
flag = False
for i in range(counter):
    data = input()
    name = re.findall(r"@(\w+)\|", data)
    age = re.findall(r"#(\d+)\*", data)
    print(f"{name[0]} is {age[0]} years old.")

# name = line[line.index("@") + 1:line.index("|")]
# age = line[line.index("#") + 1:line.index("*")]