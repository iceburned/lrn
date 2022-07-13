import re

data = input()
regex = r"(?<=(@|#))[A-Za-z]{3,}\1\1[A-Za-z]{3,}(?=\1)"
operation = re.finditer(regex, data)
lst = [_.group() for _ in operation]
lst2 = []
if lst:
    print(f"{len(lst)} word pairs found!")
else:
    print("No word pairs found!")
for i in lst:
    if "#" in i:
        first, second = i.split("##")
        if first == second[::-1]:
            lst2.append(f"{first} <=> {second}")
    elif "@" in i:
        first, second = i.split("@@")
        if first == second[::-1]:
            lst2.append(f"{first} <=> {second}")
if lst2:
    print("The mirror words are:")
    print(", ".join(lst2))
else:
    print('No mirror words!')
