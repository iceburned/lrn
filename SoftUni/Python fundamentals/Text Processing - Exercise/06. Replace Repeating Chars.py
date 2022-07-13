data = input()
answer = ''
flag = ''
for i in data:
    if not i == flag:
        answer += ''.join(i)
        flag = i
print(answer)