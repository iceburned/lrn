messages_capacity = int(input())
dkt = {}
command = input()
while not command == "Statistics":
    if command.startswith("Add"):
        comm, user, sent, received = command.split("=")
        if user not in dkt:
            dkt.update({user: {"sent": int(sent), "received": int(received)}})
    elif command.startswith("Message"):
        comm, sender, receiver = command.split("=")
        if sender in dkt and receiver in dkt:
            dkt[sender]["sent"] += 1
            if dkt[sender]["sent"] + dkt[sender]["received"] >= messages_capacity:
                dkt.pop(sender)
                print(f"{sender} reached the capacity!")
            dkt[receiver]["received"] += 1
            if dkt[receiver]["received"] + dkt[receiver]["sent"] >= messages_capacity:
                dkt.pop(receiver)
                print(f"{receiver} reached the capacity!")
    elif command.startswith("Empty"):
        comm, user = command.split("=")
        if user == "All":
            dkt.clear()
        else:
            if user in dkt:
                dkt.pop(user)
    command = input()
print(f"Users count: {len(dkt.keys())}")
for s in dkt:
    print(f"{s} - {dkt[s]['sent'] + dkt[s]['received']}")
