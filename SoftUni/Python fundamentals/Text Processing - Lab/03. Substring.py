keyword = input()
data = input()
while keyword in data:
    data = data.replace(keyword, '')
print(data)
