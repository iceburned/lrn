loot = input().split("|")
action = input()
while not action == "Yohoho!":
    action = action.split(' ')
    if action[0] == "Loot":
        for i in action[1:]:
            if i not in loot:
                loot.insert(0, i)
    elif action[0] == "Drop":
        index = int(action[1])
        if 0 <= index < len(loot):
            index_loot = loot[index]
            loot.pop(index) and loot.append(index_loot)
    elif action[0] == "Steal":
        index_steal = int(action[1])
        if 0 <= index_steal:
            steal_items = loot[-index_steal:]
            loot = loot[:-index_steal]
            print(', '.join(steal_items))
    action = input()
if loot:
    answer = sum([len(_) for _ in loot]) / len(loot)
    print(f"Average treasure gain: {answer:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
