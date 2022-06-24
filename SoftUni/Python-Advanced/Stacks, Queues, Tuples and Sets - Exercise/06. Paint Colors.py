from collections import deque

info = deque([x for x in input().split()])

main_colours = (
    'red',
    'yellow',
    'blue'
)
secondary_colours = (
    'orange',
    'purple',
    'green'
)

collected_colours = list()
final_list = list()

forming_colours = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}

while info:
    if len(info) == 1:
        first = info.popleft()
        second = ''
    else:
        first = info.popleft()
        second = info.pop()

    if first + second in main_colours:
        collected_colours.append(first + second)
        continue
    if second + first in main_colours:
        collected_colours.append(second + first)
        continue
    if first + second in secondary_colours:
        collected_colours.append(first + second)
        continue
    if second + first in secondary_colours:
        collected_colours.append(second + first)
        continue

    if len(first) > 1:
        info.insert((len(info) // 2), first[:-1])
    if len(second) > 1:
        info.insert((len(info) // 2), second[:-1])

for colour in collected_colours:
    if colour in main_colours:
        final_list.append(colour)
    if colour in secondary_colours:
        if forming_colours[colour][0] in collected_colours and forming_colours[colour][1] in collected_colours:
            final_list.append(colour)

print(final_list)
