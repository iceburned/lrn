import re

data = input()
regex = r"(@|#)+(?P<color>[a-z]{3,})(@|#)+\W*/+(?P<amount>\d+)/+"
operation = re.finditer(regex, data)
for s in operation:
    print(f"You found {s.group('amount')} {s.group('color')} eggs!")
