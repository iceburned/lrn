data = [_.strip().split() for _ in input().split("|")]
for s in range(len(data)-1, -1, -1):
    for ss in data[s]:
        print(ss, end=' ')
