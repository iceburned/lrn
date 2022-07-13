data = input().split("\\")
word = data[-1:]
name, extension = word[0].split(".")
print(f"File name: {name}\nFile extension: {extension}")
