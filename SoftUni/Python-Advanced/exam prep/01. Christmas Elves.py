from collections import deque


elf_energy = deque(int(_) for _ in input().split())
materials = deque(int(_) for _ in input().split())
santa_bag = 0
count = 0
energy = 0

while elf_energy and materials:
    single_energy = elf_energy.popleft()
    single_material = materials.pop()
    count += 1

    if single_energy < 5:
        materials.append(single_material)
    elif count % 3 == 0 and count % 5 == 0:
        if single_energy >= single_material * 2:
            single_energy -= single_material * 2
            energy += single_material * 2
            elf_energy.append(single_energy)
        else:
            elf_energy.append(single_energy * 2)
            materials.append(single_material)
    elif count % 3 == 0:
        if single_energy >= single_material * 2:
            single_energy -= single_material * 2
            single_energy += 1
            santa_bag += 2
            energy = single_material * 2
            elf_energy.append(single_energy)
        else:
            elf_energy.append(single_energy * 2)
            materials.append(single_material)
    elif count % 5 == 0:
        if single_energy >= single_material:
            single_energy -= single_material
            energy += single_material
            elf_energy.append(single_energy)
        else:
            elf_energy.append(single_energy * 2)
            materials.append(single_material)
    elif single_energy >= single_material:
        single_energy -= single_material
        single_energy += 1
        santa_bag += 1
        energy += single_material
        elf_energy.append(single_energy)
    else:
        elf_energy.append(single_energy * 2)
        materials.append(single_material)
print(f"Toys: {santa_bag}\nEnergy: {energy}")
print(', '.join(map(str, elf_energy)))
