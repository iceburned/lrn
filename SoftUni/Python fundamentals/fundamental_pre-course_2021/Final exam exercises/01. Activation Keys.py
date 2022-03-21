def contains(my_str, substring):
    if substring in my_str:
        print(f"{my_str} contains {substring}")
    else:
        print("Substring not found!")


def flip(my_str, act, start, end):
    start = int(start)
    end = int(end)
    if start <= len(my_str) > end:
        if act == "Upper":
            my_str = my_str[:start] + my_str[start:end].upper() + my_str[end:]
        elif act == "Lower":
            my_str = my_str[:start] + my_str[start:end].lower() + my_str[end:]
    return my_str


def slice(my_str, start, end):
    start = int(start)
    end = int(end)
    if start <= len(my_str) > end:
        my_str = my_str[:start] + my_str[end:]
    return my_str


data = input()
data_input = input()
while not data_input == "Generate":
    if data_input.startswith("Contains"):
        comm, sub = data_input.split(">>>")
        contains(data, sub)
    elif data_input.startswith("Flip"):
        comm, action, start_index, end_index = data_input.split(">>>")
        data = flip(data, action, start_index, end_index)
        print(data)
    elif data_input.startswith("Slice"):
        comm, start_index, end_index = data_input.split(">>>")
        data = slice(data, start_index, end_index)
        print(data)
    data_input = input()
print(f"Your activation key is: {data}")
