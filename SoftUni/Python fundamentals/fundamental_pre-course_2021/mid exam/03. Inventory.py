lst = input().split(", ")
data = input()
while data != "Craft!":
    data = data.split(" - ")
    if "Collect" in data:
        if data[1] not in lst:
            lst.append(data[1])
    elif "Drop" in data:
        if data[1] in lst:
            lst.remove(data[1])
    elif "Combine Items" in data:
        old_item, new_item = data[1].split(":")
        if old_item in lst:
            index = lst.index(old_item)
            lst.insert(index+1, new_item)
    elif "Renew" in data:
        if data[1] in lst:
            lst.remove(data[1])
            lst.append(data[1])
    data = input()
print(', '.join(lst))
