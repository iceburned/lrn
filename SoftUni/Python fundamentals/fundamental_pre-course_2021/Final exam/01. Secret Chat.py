def insert_space(code, index):
    if index < len(code):
        code = code[:index] + " " + code[index:]
    print(code)
    return code


def reverse(code, substring):
    code = code.replace(substring, "", 1)
    code = code + substring[::-1]
    print(code)
    return code


def change_all(code, substring, replacement):
    code = code.replace(substring, replacement)
    print(code)
    return code


secret = input()
data = input()
while not data == "Reveal":
    data = data.split(":|:")
    if data [0] == "InsertSpace":
        ind = int(data[1])
        secret = insert_space(secret, ind)
    elif data[0] == "Reverse":
        if data[1] in secret:
            secret = reverse(secret, data[1])
        else:
            print("error")
    elif data[0] == "ChangeAll":
        substr = data[1]
        replace = data[2]
        secret = change_all(secret, substr, replace)
    data = input()
print("You have a new text message: " + secret)
