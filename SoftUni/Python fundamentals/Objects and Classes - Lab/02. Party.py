class Party:
    def __int__(self):
        self.people = []


party = Party()
line = input()
while not line == "End":
    party.people.append(line)
    line = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(line)}")
