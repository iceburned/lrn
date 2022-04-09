mtx = []
for _ in range(int(input())):
    mtx.append(input().split(", "))
answer = []
[[answer.append(int(a)) for a in _] for _ in mtx]
print(answer)
