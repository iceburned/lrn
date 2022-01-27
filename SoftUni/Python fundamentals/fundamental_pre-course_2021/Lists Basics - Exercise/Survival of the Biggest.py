list_input = input().split()
count = int(input())
lst = [int(i) for i in list_input]
lst1 = lst.copy()
lst1.sort()
for a in range(count):
    if lst1[a] in lst:
        lst.remove(lst1[a])
print(', '.join(str(b) for b in lst))
