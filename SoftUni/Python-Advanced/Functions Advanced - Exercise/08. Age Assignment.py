def age_assignment(*args, **kwargs):
    names = args
    age = kwargs
    # dkt = {}
    # for n in names:
    #     if n[0] in age:
    #         dkt.update({n: age[n[0]]})
    # dkt = dict(sorted(dkt.items()))
    # return [''.join(f"{k} is {v} years old.") for k, v in dkt.items()]
    dkt = {x: age[x[0]] for x in names}
    dkt = dict(sorted(dkt.items()))


print(age_assignment("Peter", "George", G=26, P=19))