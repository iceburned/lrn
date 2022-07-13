ban_list = input().split(", ")
text = input()
for i in ban_list:
    asterix = len(i)
    text = text.replace(i, "*" * asterix)
print(text)
