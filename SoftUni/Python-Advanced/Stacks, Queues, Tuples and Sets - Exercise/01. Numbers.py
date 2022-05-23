first = set(map(int, input().split(" ")))
second = set(map(int, input().split(" ")))
for _ in range(int(input())):
    data = input().split(" ")
    digits = [int(_) for _ in data if _.isdigit()]
    command = data[0]
    action = data[1]
    if command.startswith("Add"):
        if action.startswith("First"):
            [first.add(_) for _ in digits]
        elif action.startswith("Second"):
            [second.add(_) for _ in digits]
    elif command.startswith("Remove"):
        if action.startswith("First"):
            [first.discard(_) for _ in digits]
        elif action.startswith("Second"):
            [second.discard(_) for _ in digits]
    elif command.startswith("Check"):
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
