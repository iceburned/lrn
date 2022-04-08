data = set()
for _ in range(int(input())):
    action, num = input().split(", ")
    if action == "IN":
        data.add(num)
    elif action == "OUT":
        data.remove(num)
if data:
    for s in data:
        print(s)
else:
    print("Parking Lot is Empty")
