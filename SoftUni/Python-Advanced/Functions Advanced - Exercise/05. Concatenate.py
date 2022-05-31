def concatenate(*args, **kwargs):
    strings = ''.join(args)
    dkt = kwargs
    for k, v in dkt.items():
        strings = strings.replace(k, v)
    return strings


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
