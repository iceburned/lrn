import re

attacked = []
destroyed = []
for i in range(int(input())):
    message = input()
    count = len(re.findall(r"[starSTAR]", message))
    new_message = ''
    for s in message:
        transfer = chr(ord(s) - count)
        new_message += ''.join(transfer)
    encripted_message = r"@(?P<name>[A-Za-z]+)[^@!:>-]*:(?P<population>\d+)" \
                        r"[^@!:>-]*!(?P<attack>A|D)\D*\![^@!:>-]*->(?P<soldiers>[\d]+)"
    encripted_regex = re.finditer(encripted_message, new_message)
    for ss in encripted_regex:
        if ss.group("attack") == "A":
            attacked.append(ss.group("name"))
        elif ss.group("attack") == "D":
            destroyed.append(ss.group("name"))
attacked = sorted(attacked, key=lambda x: x)
destroyed = sorted(destroyed, key=lambda x: x)
print(f"Attacked planets: {len(attacked)}")
for a in attacked:
    print(f"-> {a}")
print(f"Destroyed planets: {len(destroyed)}")
for b in destroyed:
    print(f"-> {b}")
