data = set()
for s in range(int(input())):
    guest = input()
    data.add(guest)
guest = input()
people = set()
while not guest == "END":
    people.add(guest)
    guest = input()
answer = data.difference(people)
print(len(answer))
for ss in sorted(answer):
    print(ss)
