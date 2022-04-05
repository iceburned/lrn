lst = []
for _ in range(int(input())):
    command = input()
    if command.startswith("1"):
        comm, num = command.split(" ")
        lst.append(int(num))
    elif command.startswith("2"):
        if lst:
            lst.pop()
    elif command.startswith("3"):
        if lst:
            print(max(lst))
    elif command.startswith("4"):
        if lst:
            print(min(lst))
stack = []
while lst:
    stack.append(str(lst.pop()))
print(", ".join(stack))
