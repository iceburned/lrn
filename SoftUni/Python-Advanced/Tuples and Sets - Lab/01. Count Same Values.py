data = (input()).split(" ")
lst = []
for s in data:
    count = data.count(s)
    if s not in lst:
        print(f"{float(s):.1f} - {count} times")
    lst.append(s)
