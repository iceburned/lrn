import re

runer = input().split(", ")
data = input()
competitors = {}
while not data == "end of race":
    regex_name = r"[A-Za-z0-9]"
    operation = re.findall(regex_name, data)
    alphas = ''
    for s in operation:
        if s.isalpha():
            alphas += ''.join(s)
    digits = 0
    for d in operation:
        if d.isdigit():
            digits += int(d)
    if alphas not in competitors and alphas in runer:
        competitors.update({alphas: 0})
        competitors[alphas] += digits
    elif alphas in competitors and alphas in runer:
        competitors[alphas] += digits
    data = input()
competitors = sorted(competitors.items(), key=lambda x: -x[1])
a = 1
for i in range(3):
    if i == 0:
        print(f"1st place: {competitors[i][0]}")
    elif i == 1:
        print(f"2nd place: {competitors[i][0]}")
    elif i == 2:
        print(f"3rd place: {competitors[i][0]}")
