lst = input().split(', ')
lst1 = input().split()
answer = []
for a in lst:
    for b in lst1:
        if a in b:
            answer.append(a)
            break
print(answer)
