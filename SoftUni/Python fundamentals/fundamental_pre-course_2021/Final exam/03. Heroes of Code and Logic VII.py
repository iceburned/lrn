def castspell(my_dict, hero_name, m, spell_name):
    if my_dict[hero_name]["mp"] >= m:
        my_dict[hero_name]["mp"] -= m
        print(f"{hero_name} has successfully cast {spell_name} and now has {my_dict[hero_name]['mp']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return my_dict


def heal(my_dict, name, amount):
    if my_dict[name]["hp"] + amount >= 100:
        temp_amount = 100 - my_dict[name]["hp"]
        my_dict[name]["hp"] = 100
        print(f"{name} healed for {temp_amount} HP!")
    else:
        my_dict[name]["hp"] += amount
        print(f"{name} healed for {amount} HP!")
    return my_dict


def recharge(my_dict, name, amount):
    if my_dict[name]["mp"] + amount >= 200:
        temp_amount = 200 - my_dict[name]["mp"]
        my_dict[name]["mp"] = 200
        print(f"{name} recharged for {temp_amount} MP!")
    else:
        my_dict[name]["mp"] += amount
        print(f"{name} recharged for {amount} MP!")
    return my_dict


def takedamage(my_dict, name, damaged, attack):
    my_dict[name]["hp"] -= damaged
    if my_dict[name]["hp"] > 0:
        print(f"{name} was hit for {damaged} HP by {attack} and now has {my_dict[name]['hp']} HP left!")
    else:
        print(f"{name} has been killed by {attack}!")
        dkt.pop(name)
    return my_dict


num_of_heroes = int(input())
dkt = {}
for _ in range(num_of_heroes):
    hero, hp, mp = input().split(" ")
    hp = int(hp)
    mp = int(mp)
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 100
    dkt.update({hero: {"hp": hp, "mp": mp}})
data = input()
while not data == "End":
    if data.startswith("CastSpell"):
        comm, hero_name, mana, spell = data.split(" - ")
        mana = int(mana)
        dkt = castspell(dkt, hero_name, mana, spell)
    elif data.startswith("Heal"):
        comm, hero_name, amount_heal = data.split(" - ")
        amount_heal = int(amount_heal)
        dkt = heal(dkt, hero_name, amount_heal)
    elif data.startswith("Recharge"):
        comm, hero_name, amount_mp = data.split(" - ")
        amount_mp = int(amount_mp)
        dkt = recharge(dkt, hero_name, amount_mp)
    elif data.startswith("TakeDamage"):
        comm, hero_name, damage, attacker = data.split(" - ")
        damage = int(damage)
        dkt = takedamage(dkt, hero_name, damage, attacker)
    data = input()
for s in dkt:
    print(f"{s}\n  HP: {dkt[s]['hp']}\n  MP: {dkt[s]['mp']}")
