parentheses = [_ for _ in input()]
lst_temp = []
flag = True
for i in parentheses:
    if i == "{" or i == "[" or i == "(":
        lst_temp.append(i)
    elif not lst_temp:  # check if lst_temp is empty
        flag = False
        break
    elif i == ")" and lst_temp[-1] == "(":
        lst_temp.pop()
    elif i == "}" and lst_temp[-1] == "{":
        lst_temp.pop()
    elif i == "]" and lst_temp[-1] == "[":
        lst_temp.pop()
    else:
        flag = False
        break
if flag and not any(lst_temp):  # check also if lst_temp is empty for balanced
    print("YES")
else:
    print("NO")
