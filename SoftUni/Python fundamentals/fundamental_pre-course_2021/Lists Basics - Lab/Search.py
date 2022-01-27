num = int(input())
code_word = input()
lst = []
lst1 = []
for _ in range(0, num):
    data = input()
    lst.append(data)
    if code_word in data:
        lst1.append(data)
print(lst)
print(lst1)
