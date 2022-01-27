lst = [int(_) for _ in input().split(', ')]
beggars = [0 for _ in range(int(input()))]
sxsx = 0
for a in range(len(lst)):
    if sxsx == len(beggars):
        sxsx = 0
    beggars[sxsx] += lst[a]
    sxsx += 1
print(beggars)


# beggars = input().split(", ")
# beggars = list(map(int, beggars))
# count_of_beggars = int(input())
# wealth = []
# if len(beggars) < count_of_beggars:
#     difference = count_of_beggars - len(beggars)
#     for diff in range(difference):
#         beggars.append(0)
# for count in range(count_of_beggars):
#     sum_elem = 0
#     index = count
#     while index < len(beggars):
#         sum_elem += beggars[index]
#         index += count_of_beggars
#     wealth.append(sum_elem)
# print(wealth)
#wtoro reshenie
string = list(map(int, input().split(", ")))
beggars = [0 for i in range(int(input()))]

indx = 0

for i in range(len(string)):
    if indx == len(beggars):
        indx = 0
    beggars[indx] += string[i]
    indx += 1

print(beggars)
