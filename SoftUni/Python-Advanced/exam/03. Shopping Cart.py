def shopping_cart(*args):
    data = args
    dkt = {'Soup': [], 'Pizza': [], 'Dessert': []}

    for t in args:
        if t == "Stop":
            break
        if t[0] == 'Soup' and len(dkt[t[0]]) < 3 and t[1] not in dkt[t[0]]:
            dkt[t[0]] += [t[1]]
        if t[0] == 'Pizza' and len(dkt[t[0]]) < 4 and t[1] not in dkt[t[0]]:
            dkt[t[0]] += [t[1]]
        if t[0] == 'Dessert' and len(dkt[t[0]]) < 2 and t[1] not in dkt[t[0]]:
            dkt[t[0]] += [t[1]]

    for k, v in dkt.items():
        dkt[k] = sorted(v)

    asd = dict(sorted(dkt.items(), key=lambda x: (-len(x[1]), x[0])))

    lst = []
    for k, v in asd. items():
        lst.append(f'{k}:')
        for vv in v:
            lst.append(f" - {vv}")

    if dkt['Soup'] or dkt['Pizza'] or dkt['Dessert']:
        return '\n'.join(lst)
    else:
        return 'No products in the cart!'








print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))