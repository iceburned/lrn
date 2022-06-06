def start_spring(**kwargs):
    dkt = kwargs
    asd = {}
    for k, v in dkt.items():
        if v not in asd:
            asd[v] = []
        asd[v].append(k)
    asd = dict(sorted(asd.items(), key=lambda x: (-len(x[1]), x[0])))
    for k, v in asd.items():
        asd[k] = sorted(v)
    zxc = []
    for k, v in asd.items():
        zxc.append(f"{k}:")
        for ii in v:
            zxc.append(f"-{ii}")
    return '\n'.join(zxc)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))