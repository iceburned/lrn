def age_assignment(*args, **kwargs):
    names = args
    age = kwargs
    dkt = {}
    for n in names:
        if n[0] in age:
            dkt.update({n: age[n[0]]})
    sorted_result = [f"{k} is {v} years old." for k, v in sorted(dkt.items(), key=lambda x: x[0])]
    return '\n'.join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))