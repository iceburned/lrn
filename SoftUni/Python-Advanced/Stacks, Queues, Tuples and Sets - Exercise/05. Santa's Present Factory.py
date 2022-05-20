from collections import deque


class SantaPresent:
    dkt = {150: "Doll",
           250: "Wooden train",
           300: "Teddy bear",
           400: "Bicycle"}

    def __init__(self, materials, magic):
        self.materials = materials
        self.magic = magic
        self.temp_box = {}
        self.flag = False
        SantaPresent.maincycle(self, materials, magic)

    def maincycle(self, materials, magic):
        while materials and magic:
            self.zero_or_one()
            if not materials or not magic:
                break
            sum_sum = materials[-1] * magic[0]
            if sum_sum <= 0:
                self.if_negative_number()
            elif sum_sum in SantaPresent.dkt:
                self.add_to_temp_box(sum_sum)
                self.remove_material_magic()
            elif sum_sum not in SantaPresent.dkt:
                self.not_in_dkt()
        self.flag_mark()
        self.print_output()

    def add_to_temp_box(self, sum_sum):
        if SantaPresent.dkt[sum_sum] not in self.temp_box:
            self.temp_box[SantaPresent.dkt[sum_sum]] = 0
        self.temp_box[SantaPresent.dkt[sum_sum]] += 1

    def remove_material_magic(self):
        self.materials.pop()
        self.magic.popleft()

    def if_negative_number(self):
        subtract = self.materials[-1] + magic[0]
        self.remove_material_magic()
        self.materials.append(subtract)

    def not_in_dkt(self):
        self.magic.popleft()
        self.materials[-1] += 15

    def zero_or_one(self):
        if self.materials[-1] == 0:
            self.materials.pop()
        elif self.magic[0] == 0:
            self.magic.popleft()

    def flag_mark(self):
        first_pair = "Doll" in self.temp_box and "Wooden train" in self.temp_box
        second_pair = "Teddy bear" in self.temp_box and "Bicycle" in self.temp_box
        if first_pair or second_pair:
            self.flag = True

    def print_output(self):
        if self.flag:
            print("The presents are crafted! Merry Christmas!")
        else:
            print("No presents this Christmas!")
        if self.materials:
            print(f"Materials left: {', '.join(map(str, self.materials))}")
        if self.magic:
            print(f"Magic left: {', '.join(map(str, self.magic))}")
        for k,v in self.temp_box.items():
            print(f"{k}: {v}")


materials = deque(int(_) for _ in input().split())
magic = deque(int(_) for _ in input().split())
a = SantaPresent(materials, magic)
