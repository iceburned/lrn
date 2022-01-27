b = []
c = []
a = [b.append(_) for _ in input()]
for i in b:
    if i.isupper():
        if not c:
            c.append(b.index(i))
        else:
            z = c[-1]
            c.append(b.index(i, z))
print(c)
