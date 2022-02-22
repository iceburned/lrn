status_pirate_ship = [int(_) for _ in input().split(">")]
status_warship = [int(_) for _ in input().split(">")]
max_health = int(input())
command = input()
flag = True
while not command == "Retire" and flag is True:
    command = command.split(' ')
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_warship):
            status_warship[index] -= damage
            if status_warship[index] <= 0:
                flag = False
                print("You won! The enemy ship has sunken.")
                break
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(status_pirate_ship) and 0 <= end_index < len(status_pirate_ship):
            for i in range(start_index, end_index + 1):
                status_pirate_ship[i] -= damage
                if status_pirate_ship[i] <= 0:
                    flag = False
                    print("You lost! The pirate ship has sunken.")
                    break
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(status_pirate_ship):
            status_pirate_ship[index] = min(status_pirate_ship[index] + health, max_health)
    elif command[0] == "Status":
        repair_count = [_ for _ in status_pirate_ship if _ < max_health * 0.2]
        print(f"{len(repair_count)} sections need repair.")
    command = input()
if flag:
    print(f"Pirate ship status: {sum(status_pirate_ship):.0f}\n"
          f"Warship status: {sum(status_warship):.0f}")
