data = input()
lst = []
for s in range(len(data)):
    if data[s] == "(":
        lst.append(s)
    elif data[s] == ")":
        stack = lst.pop()
        print(data[stack:s + 1])
