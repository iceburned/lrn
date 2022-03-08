data = input().split(", ")
flag = True
for i in data:
    flag = True
    if 3 <= len(i) <= 16:
        for s in i:
            if not s.isdigit() and not s.isalpha() and not s == "-" and not s == "_":
                flag = False
                break
        if flag:
            print(i)
