count = int(input())
dkt = {}
for _ in range(count):
    data = input().split(' ')
    if "unregister" in data:
        reg_type, username = data
        if username not in dkt:
            print(f"ERROR: user {username} not found")
        else:
            del dkt[username]
            print(f"{username} unregistered successfully")
    elif "register" in data:
        reg_type, username, license_plate = data
        if username in dkt:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            dkt[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
for key, value in dkt.items():
    print(f"{key} => {value}")
