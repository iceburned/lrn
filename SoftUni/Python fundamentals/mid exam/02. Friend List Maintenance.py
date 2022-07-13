lst = input().split(", ")
data = input()
blacklisted = 0
lost = 0
while not data == "Report":
    data = data.split(" ")
    if data[0] == "Blacklist":
        if data[1] in lst:
            print(f"{data[1]} was blacklisted.")
            lst = list(map(lambda item: item.replace(data[1], "Blacklisted"), lst))
            blacklisted += 1
        else:
            print(f"{data[1]} was not found.")
    elif data[0] == "Error" and 0 <= int(data[1]) < len(lst):
        index = int(data[1])

        if lst[index] != "Blacklisted" and lst[index] != "Lost":
            print(f"{lst[index]} was lost due to an error.")
            lst = list(map(lambda item: item.replace(lst[index], "Lost"), lst))
            lost += 1
    elif data[0] == "Change":
        index = int(data[1])
        new_name = data[2]
        if 0 <= index < len(lst):
            print(f"{lst[index]} changed his username to {new_name}.")
            lst = list(map(lambda item: item.replace(lst[index], new_name), lst))
    data = input()
print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(*lst)
