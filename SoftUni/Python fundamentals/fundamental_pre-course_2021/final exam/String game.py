data_str = input()
command = input()
while not command == "Done":
    if command.startswith("Change"):
        comm, char, repl = command.split(" ")
        data_str = data_str.replace(char, repl)
        print(data_str)
    elif command.startswith("Includes"):
        comm, sub_str = command.split(" ")
        if sub_str in data_str:
            print("True")
        else:
            print("False")
    elif command.startswith("End"):
        comm, sub_str = command.split(" ")
        if data_str.endswith(sub_str):
            print("True")
        else:
            print("False")
    elif command.startswith("Uppercase"):
        data_str = data_str.upper()
        print(data_str)
    elif command.startswith("FindIndex"):
        comm, ch = command.split(" ")
        index = data_str.find(ch)
        print(index)
    elif command.startswith("Cut"):
        comm, start_indx, count = command.split(" ")
        start_indx = int(start_indx)
        data_str = data_str[start_indx:start_indx + int(count)]
        print(data_str)
    command = input()
