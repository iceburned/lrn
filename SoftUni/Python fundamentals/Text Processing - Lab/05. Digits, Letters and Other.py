data = input()
letters = str()
numbers = str()
characters = str()
for i in data:
    if i.isdigit():
        numbers += i
    elif i.isalpha():
        letters += i
    else:
        characters += i
print(numbers)
print(letters)
print(characters)
