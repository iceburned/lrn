from collections import deque


elf_energy = deque(int(_) for _ in input().split())
materials = [int(_) for _ in input().split()]
santa_bag = 0
count = 0
energy = 0

while elf_energy and materials:
    single_energy = elf_energy.popleft()
    single_material = materials.pop()
    count += 1
    if single_energy < 5:
        materials.append(single_material)
        continue
    elif count % 3 == 0:
        if single_energy >= single_material * 2:
            if count % 5 == 0:
                energy += single_material * 2

                elf_energy.append(single_energy - single_material * 2)
                continue
            else:
                energy += single_material * 2
                santa_bag += 2
                elf_energy.append(single_energy + 1 - single_material * 2)
                continue
        else:
            elf_energy.append(single_energy * 2)
            materials.append(single_material)
            continue
    if count % 5 == 0:
        if single_energy >= single_material:
            energy += single_material
            elf_energy.append(single_energy - single_material)
            continue
        else:
            elf_energy.append(single_energy * 2)
            materials.append(single_material)
            continue
    if single_energy >= single_material:
        santa_bag += 1
        energy += single_material
        elf_energy.append(single_energy - single_material + 1)
    else:
        elf_energy.append(single_energy * 2)
        materials.append(single_material)

print(f'Toys: {santa_bag}')
print(f'Energy: {energy}')
if elf_energy:
    print(f'Elves left: {", ".join([str(x) for x in elf_energy])}')
if materials:
    print(f'Boxes left: {", ".join([str(x) for x in materials])}')
