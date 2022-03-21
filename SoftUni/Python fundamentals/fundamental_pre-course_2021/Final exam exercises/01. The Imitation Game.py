def change(code, substring, replacement):
    for i in code:
        if i == substring:
            code = code.replace(substring, replacement, 1)
    return code


def insert(code, index, value):
    index = int(index)
    code = [''.join(_) for _ in code]
    code.insert(index, value)
    return ''.join(code)


def move(code, num_letters):
    num_letters = int(num_letters)
    code = code[num_letters:] + code[:num_letters]
    return code


code = input()
data = input()
codename = ''
while not data == "Decode":
    data = data.split("|")
    if "ChangeAll" in data:
        code = change(code, data[1], data[2])
    elif "Insert" in data:
        code = insert(code, data[1], data[2])
    elif "Move" in data:
        code = move(code, data[1])
    data = input()
print(f"The decrypted message is: {code}")
