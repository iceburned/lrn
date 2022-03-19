import re

lst = []
for i in range(int(input())):
    barcode = input()
    regex = r"(@\#{1,})(?P<asd>[A-Z]([A-Za-z0-9]+){4,}[A-Z])(@\#{1,})"
    reg_match = re.finditer(regex, barcode)
    if re.search(regex, barcode):
        for z in reg_match:
            lst.append(z.group("asd"))
            temp_num = ""
            for ss in z.group("asd"):
                if ss.isdigit():
                    temp_num += ''.join(ss)
            if temp_num:
                print(f"Product group: {temp_num}")
            else:
                print(f"Product group: 00")
    else:
        print("Invalid barcode")




