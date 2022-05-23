from collections import deque


def secondary_color(color):
    if color == "orange":
        if "red" and " yellow" in main_colors:
            m_colors.append(color)
            return True
    elif color == "purple":
        if "red" and "blue" in main_colors:
            m_colors.append(color)
            return True
    elif color == "green":
        if "yellow" and "blue" in main_colors:
            m_colors.append(color)
            return True
    return False


def main_color(d):
    temp_color = d[0] + d[-1]
    if temp_color in main_colors:
        m_colors.append(temp_color)
        return True
    elif temp_color in secondary_colors:
        sc = secondary_color(temp_color)
        return sc
    temp_color = d[-1] + d[0]
    if temp_color in main_colors:
        m_colors.append(temp_color)
        return True
    elif temp_color in secondary_colors:
        sc = secondary_color(temp_color)
        return sc
    return False


def remove_first_last_character(d):
    frst_str = d[0]
    sec_str = d[-1]
    d[0] = frst_str[:-1]
    d[-1] = sec_str[:-1]
    return d


def remove_first_last_elements(d):
    d.pop()
    d.pop(0)
    return d


def shuffle_places(d):
    length = len(d) // 2
    if len(d) % 2 != 0:
        d.insert(length + 1, d.pop(-1))
        d.insert(length + 1, d.pop(0))
    else:
        d.insert(length, d.pop(-1))
        d.insert(length, d.pop(0))
    d = list(filter(None, d))
    return d


def single_color(d):
    if d[0] in main_colors:
        m_colors.append(d[0])
        return []
    elif d[0] in secondary_colors:
        sc = secondary_color(d[0])
        if sc:
            return []
    return d


main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
m_colors = []
data = input().split()
while data:
    if len(data) == 1:
        data = single_color(data)
    elif main_color(data):
        data = remove_first_last_elements(data)
    else:
        data = remove_first_last_character(data)
        data = shuffle_places(data)

print(m_colors)
