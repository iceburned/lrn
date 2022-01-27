lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
helmet_flag = False
sword_flag = False
shield_count = 0
for i in range(1, lost_fight_count + 1):
    if i % 2 == 0:
        broken_helmet += helmet_price
        helmet_flag = True
    if i % 3 == 0:
        broken_sword += sword_price
        sword_flag = True
    if helmet_flag and sword_flag:
        broken_shield += shield_price
        shield_count += 1
    if shield_count >= 2:
        broken_armor += armor_price
        shield_count = 0
    helmet_flag = False
    sword_flag = False
print(f"Gladiator expenses: {broken_helmet + broken_sword + broken_shield + broken_armor:.2f} aureus")
