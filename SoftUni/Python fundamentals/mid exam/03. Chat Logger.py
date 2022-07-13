lst = []
data = input()
while data != "end":
    data = data.split(" ")
    if data[0] == "Chat" and data[1] not in lst:
        lst.append(data[1])
    elif data[0] == "Delete" and data[1] in lst:
        lst.remove(data[1])
    elif data[0] == "Edit" and data[1] in lst:
        old_message = data[1]
        new_message = data[2]
        # lst = list(map(lambda item: item.replace(old_message, new_message), lst))
        for s in range(len(lst)):
            if lst[s] == old_message:
                lst[s] = new_message

    elif data[0] == "Pin" and data[1] in lst:
        word = data[1]
        lst.remove(word)
        lst.append(word)
    elif data[0] == "Spam" and data[1] not in lst:
        lst.extend(data[1:])
    data = input()
for i in lst:
    print(i, end='\n')
