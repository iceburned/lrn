lst = input().split("!")
items = input()
while not items == "Go Shopping!":
    if "Correct" in items:
        action, old_item, new_item = items.split(' ')
        if old_item in lst:
            a = lst.index(old_item)
            lst[a] = new_item
    elif "Urgent" in items:
        action, item = items.split(' ')
        if item not in lst:
            lst.insert(0, item)
    elif "Unnecessary" in items:
        action, item = items.split(' ')
        if item in lst:
            lst.remove(item)
    elif "Rearrange" in items:
        action, item = items.split(' ')
        if item in lst:
            lst.remove(item)
            lst.append(item)
    items = input()
print(", ".join(lst))
