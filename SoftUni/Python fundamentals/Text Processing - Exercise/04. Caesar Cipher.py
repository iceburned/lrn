data = input()
new_str = ''
for i in data:
    letter = ord(i) + 3
    new_str += ''.join(chr(letter))
print(new_str)