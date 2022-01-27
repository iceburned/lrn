s = str(input())
num = 0
for i in s:
    if i == "a":
        num += 1
    elif i == "e":
        num += 2
    elif i == "i":
        num += 3
    elif i == "o":
        num += 4
    elif i == "u":
        num += 5
    else:
        pass
print(num)
